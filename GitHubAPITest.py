import unittest
from unittest import mock
import requests

from GitHubAPI import githubAPI

class GitHubAPITest(unittest.TestCase):

    #Test the input validation phase
    def testValidation(self):
        self.assertEqual(githubAPI(None), "There is no input, please enter github id", "Should enter valid input")

    def testInputType(self):
        self.assertEqual(githubAPI(1234567), "The input is not string", "Should enter input string")

    def testFirstOfMine(self):
        succes_return = mock.Mock(
            return_value=['Repo Name: CS513Stevens Commits Number:3', 'Repo Name: cs546coursework Commits Number:7',
                          'Repo Name: CS557Stevens Commits Number:2', 'Repo Name: CS559HW2 Commits Number:7',
                          'Repo Name: CS559ML Commits Number:1', 'Repo Name: EE629 Commits Number:3',
                          'Repo Name: GadgetClear Commits Number:4', 'Repo Name: jingyi199858 Commits Number:1',
                          'Repo Name: photoModule Commits Number:1', 'Repo Name: SSW555Gedcom Commits Number:30',
                          'Repo Name: SSW567 Commits Number:5', 'Repo Name: SSW567API Commits Number:7',
                          'Repo Name: ssw567hw2 Commits Number:7', 'Repo Name: taylorfit Commits Number:30',
                          'Repo Name: TeamAssignment2 Commits Number:13'])
        githubAPI = succes_return
        self.assertEqual(githubAPI("jingyi199858")[0], "Repo Name: CS513Stevens Commits Number:3", "Incorrect info retrieved")

    def testResponse(self):
        returned_value = mock.Mock(return_value=404)
        githubAPI = returned_value
        self.assertEqual(githubAPI(""), 404, "Can't retrieve info")

    def testMock(self):
        succes_return = mock.Mock(return_value=['Repo Name: CS513Stevens Commits Number:3', 'Repo Name: cs546coursework Commits Number:7', 'Repo Name: CS557Stevens Commits Number:2', 'Repo Name: CS559HW2 Commits Number:7', 'Repo Name: CS559ML Commits Number:1', 'Repo Name: EE629 Commits Number:3', 'Repo Name: GadgetClear Commits Number:4', 'Repo Name: jingyi199858 Commits Number:1', 'Repo Name: photoModule Commits Number:1', 'Repo Name: SSW555Gedcom Commits Number:30', 'Repo Name: SSW567 Commits Number:5', 'Repo Name: SSW567API Commits Number:7', 'Repo Name: ssw567hw2 Commits Number:7', 'Repo Name: taylorfit Commits Number:30', 'Repo Name: TeamAssignment2 Commits Number:13'])
        githubAPI = succes_return
        self.assertEqual(githubAPI("jingyi199858")[0], "Repo Name: CS513Stevens Commits Number:3",)