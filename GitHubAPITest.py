import unittest
import requests

from GitHubAPI import githubAPI

class GitHubAPITest(unittest.TestCase):

    #Test the input validation phase
    def testValidation(self):
        self.assertEqual(githubAPI(None), "There is no input, please enter github id", "Should enter valid input")

    def testInputType(self):
        self.assertEqual(githubAPI(1234567), "The input is not string", "Should enter input string")

    def testFirstOfMine(self):
        self.assertEqual(githubAPI("jingyi199858")[0], "Repo Name: CS513Stevens Commits Number:3", "Incorrect info retrieved")

    def testResponse(self):
        self.assertEqual(githubAPI(""), 404, "Can't retrieve info")