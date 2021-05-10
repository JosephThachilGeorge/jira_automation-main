# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url="https://jojo26.atlassian.net//rest/api/2/issue"
headers={
    "Accept": "application/json",
    "Content-Type": "application/json"
}
payload=json.dumps(
    {
    "fields": {
       "project":
       {
          "key": "JIRA"
       },
       "summary": "Created for new Task in IGT",
       "description": "Created for new Task in IGT",
       "issuetype": {
          "name": "Task"
       }
   }
}
)
response=requests.post(url,headers=headers,data=payload,auth=("josephthachilgeorge@gmail.com","bQReh7MLd5yhIVXjZUkc9836"))
data=response.json()
print(response.text)



