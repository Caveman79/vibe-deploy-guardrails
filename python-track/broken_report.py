"""Deliberately flawed review specimen. Run only with synthetic course fixtures."""
import pandas as pd
rows = pd.read_csv('fixtures/flight_intake.csv')
rows['minutes'] = pd.to_numeric(rows['minutes'], errors='coerce').fillna(0)
print('Total minutes:', rows['minutes'].sum())
# Problems to identify: duplicates, unknown missions, negative values, invalid dates,
# and silently converting unknown data to zero. A number printed is not validated evidence.
