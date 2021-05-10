import requests
import json
import io
url="https://jojo26.atlassian.net/rest/api/3/search"
headers={
  "Accept": "application/json",
    "Content-Type": "application/json"
}

query = {
   'jql': 'project = JIRA'
}

response=requests.get(url,headers=headers,params=query,auth=("josephthachilgeorge@gmail.com","XC1EOL4YkJSYiD2YDQg1DCD5"))
data=response.json()
issues=data["issues"]
for issue in issues:
    print(issue["key"])

