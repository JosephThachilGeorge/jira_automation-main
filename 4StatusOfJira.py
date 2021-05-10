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
    issue_key=issue["key"]
    url1="https://jojo26.atlassian.net/rest/api/3/issue/"+issue_key
    response=requests.get(url1,headers=headers,auth=("josephthachilgeorge@gmail.com","XC1EOL4YkJSYiD2YDQg1DCD5"))
    data=response.json()
    print(f'issue id is {issue_key} and status is {data["fields"]["status"]["name"]}')






