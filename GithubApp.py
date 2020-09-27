"""
Get and print list of repos with number of commits in each repo, from username
"""
import requests


def getReposList(username):
    resp = requests.get('https://api.github.com/users/' + username + '/repos')
    respJson = resp.json()
    return respJson


def getCommitsList(username, repoName):
    resp = requests.get('https://api.github.com/repos/' + username + '/' + repoName + '/commits')
    respJson = resp.json()
    return respJson


def listReposWithCounts(username):
    repos = getReposList(username)
    for repo in repos:
        count = len(getCommitsList(username, repo['name']))
        print("Repo: " + repo['name'] + " Number of commits: " + str(count))


listReposWithCounts("aej11a")
