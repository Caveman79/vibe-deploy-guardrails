"""Fetch all pages from the training mission API. Requires requests."""
import argparse
import json
import os
from pathlib import Path
from urllib.parse import urlsplit
import requests


def fetch_missions(base, customer=None, session=None):
    parsed = urlsplit(base)
    if parsed.username or parsed.password or parsed.query or parsed.fragment:
        raise ValueError('base URL must not contain credentials, queries or fragments')
    if parsed.scheme != 'https' and not (parsed.scheme == 'http' and parsed.hostname in {'127.0.0.1','localhost'}):
        raise ValueError('HTTP is allowed only for local practice; otherwise use HTTPS')
    client = session or requests.Session()
    offset, items = 0, []
    try:
        for _ in range(100):
            params = {'offset': offset}
            if customer is not None:
                params['customer'] = customer
            reply = client.get(base.rstrip('/')+'/api/missions', params=params, timeout=(3,5), allow_redirects=False)
            reply.raise_for_status()
            if reply.status_code != 200:
                raise ValueError('expected HTTP 200, not a redirect')
            page = reply.json()
            if not isinstance(page, dict) or not isinstance(page.get('items'), list):
                raise ValueError('unexpected response shape')
            for item in page['items']:
                if not isinstance(item, dict) or not all(isinstance(item.get(k),str) for k in ('mission_id','customer_id','status')):
                    raise ValueError('invalid mission record')
            items.extend(page['items'])
            if 'next_offset' not in page:
                raise ValueError('missing pagination marker')
            next_offset = page['next_offset']
            if next_offset is None:
                if len({x['mission_id'] for x in items}) != len(items):
                    raise ValueError('duplicate mission IDs across pages')
                return items
            if type(next_offset) is not int or next_offset <= offset:
                raise ValueError('pagination did not advance')
            offset = next_offset
        raise ValueError('page limit reached; data is incomplete')
    finally:
        if session is None:
            client.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--base', default=os.environ.get('API_BASE_URL','http://127.0.0.1:8000'))
    parser.add_argument('--customer', choices=['C01','C02'])
    parser.add_argument('--output', type=Path, default=Path('evidence/missions.json'))
    args = parser.parse_args()
    try:
        items = fetch_missions(args.base,args.customer)
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(items,indent=2)+'\n')
        print(f'Saved {len(items)} missions to {args.output}')
    except (requests.RequestException, ValueError, OSError):
        parser.exit(1,'API fetch failed; output may be absent or incomplete. Check the server, URL, HTTP status and response shape.\n')
