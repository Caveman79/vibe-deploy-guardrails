"""Validate synthetic intake and write a repeatable report. Requires requirements-data.txt."""
import argparse
import json
import logging
from pathlib import Path
import pandas as pd

LOG = logging.getLogger("intake")
COLUMNS = ["flight_id", "mission_id", "minutes", "landed_at"]


def analyze(csv_path, missions_path):
    raw = pd.read_csv(csv_path, dtype="string", keep_default_na=False)
    if list(raw.columns) != COLUMNS:
        raise ValueError("unexpected CSV columns")
    missions = pd.DataFrame(json.loads(Path(missions_path).read_text()))
    if set(missions.columns) != {"mission_id", "customer_id"} or missions['mission_id'].duplicated().any():
        raise ValueError("mission lookup must contain unique IDs and customer IDs")
    reasons = [[] for _ in range(len(raw))]
    minutes = pd.to_numeric(raw['minutes'], errors='coerce')
    dates = pd.to_datetime(raw['landed_at'], format='%Y-%m-%dT%H:%M:%SZ', errors='coerce', utc=True)
    duplicate = raw.duplicated(subset=['flight_id'], keep='first')
    conflicts = set()
    for flight_id, group in raw.groupby('flight_id'):
        if len(group.drop_duplicates()) > 1:
            conflicts.add(flight_id)
    for i, row in raw.iterrows():
        if not row['flight_id']:
            reasons[i].append('missing_id')
        if row['flight_id'] in conflicts:
            reasons[i].append('conflicting_duplicate')
        elif duplicate.iloc[i]:
            reasons[i].append('duplicate')
        if not row['minutes'].isascii() or not row['minutes'].isdigit() or pd.isna(minutes.iloc[i]) or minutes.iloc[i] <= 0:
            reasons[i].append('invalid_minutes')
        if pd.isna(dates.iloc[i]):
            reasons[i].append('invalid_time')
        if row['mission_id'] not in set(missions['mission_id']):
            reasons[i].append('unknown_mission')
    valid = pd.Series([not x for x in reasons], index=raw.index, dtype=bool)
    accepted = raw.loc[valid].copy()
    accepted['minutes'] = minutes.loc[valid].astype('int64')
    accepted = accepted.merge(missions, on='mission_id', how='left', validate='many_to_one')
    rejected = raw.loc[~valid].copy()
    rejected['reasons'] = [';'.join(reasons[i]) for i in rejected.index]
    totals = accepted.groupby('customer_id', as_index=False)['minutes'].sum().sort_values('customer_id')
    report = {'source_rows': len(raw), 'accepted_rows': len(accepted), 'rejected_rows': len(rejected), 'total_minutes': int(accepted['minutes'].sum()), 'customer_totals': totals.to_dict(orient='records')}
    return report, rejected


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--csv', type=Path, default=Path('fixtures/flight_intake.csv'))
    parser.add_argument('--missions', type=Path, default=Path('fixtures/missions.json'))
    parser.add_argument('--output', type=Path, default=Path('evidence/intake'))
    args = parser.parse_args()
    logging.basicConfig(level=logging.INFO, format='%(message)s')
    try:
        report, rejected = analyze(args.csv, args.missions)
        args.output.mkdir(parents=True, exist_ok=True)
        (args.output/'report.json').write_text(json.dumps(report, indent=2)+'\n')
        rejected.to_csv(args.output/'quarantine.csv', index=False)
        LOG.info(json.dumps({'event':'report_written', 'accepted':report['accepted_rows'], 'rejected':report['rejected_rows']}))
    except (ValueError, OSError, KeyError) as error:
        parser.exit(1, f'Analysis failed: {error}\n')
