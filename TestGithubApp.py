import sys
import unittest
from GithubApp import getReposList, getCommitsList, listReposWithCounts

class TestGithub(unittest.TestCase):
    def testGetReposList(self):
        self.assertIsNotNone(getReposList("adwqdwqdwqwdsdthtjyj")['message'])
        repos = getReposList("aej11a")
        self.assertTrue(len(repos) > 0)
        self.assertIsNotNone(repos[0]['id'])

    def testGetCommitsList(self):
        self.assertIsNotNone(getCommitsList("adwqdwqdwqwdsdthtjyj", "test")['message'])
        commits = getCommitsList("aej11a", "Mars-Weather")
        self.assertTrue(len(commits) > 0)
        self.assertIsNotNone(commits[0]['sha'])

    def testListReposWithCounts(self):
        self.assertTrue("Repo: excalidraw Number of commits: 30" in listReposWithCounts("aej11a"))