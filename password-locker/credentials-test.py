import unittest
from credentials import Credentials

class TestUser(unittest.TestCase):
    '''
    Test class that defines the test cases for user class
    behaviours
    '''
    def setUp(self):
        '''
        Setup method to run before each test cases
        '''
        self.new_credential = Credentials("twitter","muko12")
    def test_init(self):
        '''
        test_init checks if the object is initialised properly
        '''
        self.assertEqual(self.new_credential.account_name,"twitter")
        self.assertEqual(self.new_credential.password,"muko12")
    def tearDown(self):
        '''
        TearDown method that does clean up after each test case has run.
        '''
        Credentials.credentials_list = []

  