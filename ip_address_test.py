import unittest
import ip_address
import os
import re
 


class Test_Ipaddress(unittest.TestCase):
    
    # test case 1 checking if all the ip address are valid according to standards
    # The numbers should be in a range of 0-255
    # It should consist of 4 cells separated by ‘.’
    def test_IpAddressFetch(self):
        
        #storing the main function IP address in result
        result=ip_address.IpAddressFetch('access.log')


        #valid IP address regex pattern
        pattern =re.compile('''((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)''')
        
        # initializing the list objects
        valid =[]
        invalid=[]
        
        # extracting the IP addresses
        for line in result:
            Indicator = pattern.search(line)
        
            # valid IP addresses
            if Indicator:
                valid.append(line)

        
            # invalid IP addresses  
            else:
                invalid.append(line)
        
        #asserting the invalid IP address  values with the valid one using assert list values
        self.assertEqual(result,valid)



    #test case 2 to check the log file is present or not 
    def test_valid_file_exists(self):
        #eter the file name to check for its presence
        filename='access.log'

        #get the current directory 
        path=os.getcwd()

        #check for if the file is present in the current location
        if os.path.exists(f'{path}\{filename}'):
            filename='access.log'
        else:
            filename=None

        #asserting if the file is present with the name
        self.assertEqual(filename,'access.log')


    #test case 3 to check if the output list file has 10 ip address or not
    def test_output_list_length(self):

        #list of all the 10 ip addrss
        IpAddressList=ip_address.IpAddressFetch('access.log')

        #number of the ip address present in the list
        ListLength=len(IpAddressList)

        #asserting if the number of ip address we get are equal to 10
        self.assertEqual(ListLength,10)


if __name__=='__main__':
    unittest.main()