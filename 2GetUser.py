import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://jojo26.atlassian.net/rest/api/2/users/search"


headers = {
   "Accept": "application/json"
}
response=requests.get(url,headers=headers,auth=("josephthachilgeorge@gmail.com","XC1EOL4YkJSYiD2YDQg1DCD5"))
data=response.json()
print(len(data))
print(data)
for users in data:
    print(users["displayName"])
