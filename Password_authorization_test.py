import unittest
import Password_authorization
import re



class Test_PasswordAuthorization(unittest.TestCase):

    #test case 1 for comparing using diffrent methods
    def test_PasswordValidationComparission(self):

        #input value for verification
        password='Ma123-.1'

        #method one using the rules and storing the output in result set 1
        Result_set_1=Password_authorization.PasswordValidationWithRules(password)

        #method two using the regular expressions and storing the output in result set 2
        Result_set_2=Password_authorization.PasswordValidationWithRegex(password)

        #validating the results with two different methods 
        self.assertEqual(Result_set_1,Result_set_2)

    #test case 2 for checking if the password is empty
    def test_password_Empty(self):

        #input value for verification submitting the empty password
        password=''

        #method one using the rules and storing the output in result set 1 for the empty password should gove invalid password
        Result_set_1=Password_authorization.PasswordValidationWithRules(password)

        #method two using the regular expressions and storing the output in result set 2 for empty password should gove invalid password
        Result_set_2=Password_authorization.PasswordValidationWithRegex(password)

        #validating the results with two different methods 
        self.assertEqual(Result_set_1,Result_set_2)




if __name__=='__main__':
    unittest.main()