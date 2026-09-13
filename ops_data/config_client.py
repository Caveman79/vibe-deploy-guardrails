"""Local-only authentication demonstration. Never prints the credential."""
import os
import requests

def main():
    token = os.environ.get('DEMO_API_TOKEN')
    if not token:
        raise SystemExit('Load .env.demo in this terminal first.')
    try:
        response = requests.get('http://127.0.0.1:8000/api/customer-config', params={'customer':'C01'}, headers={'Authorization':'Bearer '+token}, timeout=(3,5), allow_redirects=False)
        if response.status_code != 200:
            raise SystemExit(f'Configuration request returned HTTP {response.status_code}. Check the lesson instructions.')
        value=response.json()
        if not isinstance(value,dict) or value.get('customer_id') != 'C01' or type(value.get('max_wind_kts')) is not int:
            raise ValueError('invalid configuration response')
        print(f"Customer {value['customer_id']}: max_wind_kts {value['max_wind_kts']}")
    except (requests.RequestException,ValueError):
        raise SystemExit('Configuration request failed. Check the server and response format.')

if __name__ == '__main__':
    main()
