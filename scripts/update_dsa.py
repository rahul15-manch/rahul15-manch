import requests
import datetime

USERNAME = "x29lHcEZCI"

url = "https://leetcode.com/graphql"

query = """
query recentSubmissionList($username: String!) {
  recentSubmissionList(username: $username) {
    title
    titleSlug
    timestamp
  }
}
"""

response = requests.post(
    url,
    json={"query": query, "variables": {"username": USERNAME}},
    headers={"Content-Type": "application/json"}
)

data = response.json()

if "data" in data and data["data"]["recentSubmissionList"]:
    latest = data["data"]["recentSubmissionList"][0]
    title = latest["title"]
    timestamp = int(latest["timestamp"])
    date = datetime.datetime.fromtimestamp(timestamp).strftime("%d %B %Y")

    new_content = f"""
✔ **Solved:** {title}  
📅 **Date:** {date}  
"""

    with open("README.md", "r", encoding="utf-8") as f:
        readme = f.read()

    start = "<!-- DSA-START -->"
    end = "<!-- DSA-END -->"

    updated = readme.split(start)[0] + start + "\n" + new_content + "\n" + end + readme.split(end)[1]

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(updated)
