import sys
import unittest
from unittest.mock import Mock, patch

from GithubApp import getReposList, getCommitsList, listReposWithCounts


@patch('GithubApp.requests.get')
class TestGithub(unittest.TestCase):

    sampleRepos = [{'name': 'myrepo', 'id': '123'}]
    sampleCommits = [{'sha': 'sample'}]

    def testGetReposList(self, mock_get):
        mock_get.return_value = Mock(ok=True)
        mock_get.return_value.json.return_value = TestGithub.sampleRepos

        repos = getReposList("testUser")
        self.assertTrue(len(repos) > 0)
        self.assertIsNotNone(repos[0]['id'])

    def testGetCommitsList(self, mock_get):
        mock_get.return_value = Mock(ok=True)
        mock_get.return_value.json.return_value = TestGithub.sampleCommits

        commits = getCommitsList("aej11a", "myrepo")
        self.assertTrue(len(commits) > 0)
        self.assertIsNotNone(commits[0]['sha'])

    def testListReposWithCounts(self, mock_get):
        # Mock two responses
        multiple_responses = [Mock(ok=True), Mock(ok=True)]
        multiple_responses[0].json.return_value = TestGithub.sampleRepos
        multiple_responses[1].json.return_value = TestGithub.sampleCommits
        mock_get.side_effect = multiple_responses

        self.assertTrue("Repo: myrepo Number of commits: 1" in listReposWithCounts("aej11a"))