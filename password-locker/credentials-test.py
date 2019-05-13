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

    def test_save_credential(self):
        '''
        test_save_credential tests if a new credential has been added to credentials
        list of a user
        '''
        self.new_credential.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)
    
    def test_display_credentials(self):
        '''
        test to display the credentials of a user
        '''
        self.assertEqual(Credentials.display_credentials(),Credentials.credentials_list)
    
    def test_delete_credential(self):
        '''
        test_delete_credential to see if we can remove a 
        credential from credentials list
        '''
        self.new_credential.save_credentials()
        test_credential = Credentials("test","0893uhjnv")
        test_credential.save_credentials()
        self.new_credential.delete_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)

if __name__ == '__main__':
    unittest.main()