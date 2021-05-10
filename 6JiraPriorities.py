# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url="https://jojo26.atlassian.net//rest/api/2/priority/4"

auth = HTTPBasicAuth("josephthachilgeorge@gmail.com","XC1EOL4YkJSYiD2YDQg1DCD5")

headers = {
   "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))