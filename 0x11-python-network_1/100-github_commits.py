#!/usr/bin/python3
"""
This script lists the 10 most recent commits of a GitHub repository.
Usage: ./100-github_commits.py <repository_name> <owner_name>
"""

import requests
import sys

if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"

    try:
        response = requests.get(url)
        if response.status_code == 200:
            commits = response.json()
            for commit in commits[:10]:
                sha = commit.get("sha")
                author = commit.get("commit", {}).get("author", {}).get("name")
                print(f"{sha}: {author}")
        else:
            print(
                    f"Error: Unable to fetch commits "
                    f"(status code: {response.status_code})"
            )
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
