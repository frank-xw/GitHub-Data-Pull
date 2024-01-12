from github import Github, Auth
import os
from dotenv import load_dotenv

# Authenticate and preparation
load_dotenv()

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

auth = Auth.Token(GITHUB_TOKEN)
g = Github(auth=auth)

# Define Repo
repo = g.get_repo("frank-xw/GitHub-Data-Pull")
issue = repo.get_issues(state='all')[0]

# Construct Issue Dictionary
issues = repo.get_issues()
issues_dict = {}
i = 1
for issue in issues:
    issue_dict = {}
    issue_dict['url'] = issue.url
    issue_dict['title'] = issue.title
    issue_dict['body'] = issue.body
    issue_dict['labels'] = issue.labels  # TODO: update to list
    issue_dict['comments'] = [comment.body for comment in issue.get_comments()]
    issues_dict[i] = issue_dict
    i += 1

print(issues_dict)

g.close()
