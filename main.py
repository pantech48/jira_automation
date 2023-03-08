from jira import JIRA
import requests
import base64


url = "https://luxproject.luxoft.com/jira/rest/api/2/issue/SIR-474"
token = "ODgzMTQ0NTc4NjkzOpThGMjbxpBKrvmXtnVh6R6srHsz"
headers = {
    "Authorization": "Barer " + token,
    "Content-Type": "application/json"
}
response = requests.get(url, headers=headers)

jira = JIRA(server="https://luxproject.luxoft.com/jira/", token_auth=token)

a = jira.issue("SIR-83")

print(jira.issue("SIR-83"))