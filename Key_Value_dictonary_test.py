import unittest
import Key_Value_dictonary
import os

class Test_Key_Value_dictonary(unittest.TestCase):

    # test case 1 checking if list 1 is greater than list 2 then the last key is None
    def test_noneCheck(self):
        result=Key_Value_dictonary.makeDictonary([1,2,3,4],[2,3,4])
        
        #creating a empty list to get all the key values
        temp=[]

        #getting all the key values and appending it to list (temp)
        for i in result.keys():
            temp.append(i)

        #extracting the last key value from the list    
        last_element_OF_LIST=temp[-1:] 


        #iterate over the last element and check if it is a string or integer
        for val in last_element_OF_LIST:
            if isinstance(val,str):
                isString=True
            else:
                isString=False

        #converting the list to a string
        listToStr = ' '.join([str(i) for i in last_element_OF_LIST]) 

        #converting the last element respectively
        if isString:
            listToStr=str(listToStr)
        else:
            listToStr=int(listToStr)


        #comparing if the value of the last element is None or not 
        if result[listToStr]==None:
            indicator = None
        else:
            indicator= 0

        #asserting the invalid IP address  values with the valid one using assert list values
        self.assertEqual(indicator,None)    



    # test case 2 checking if list 1 is less than list 2 then the number of keys is equal to number of values
    def test_lengthCheck(self):
        result=Key_Value_dictonary.makeDictonary([1,2,3],[2,3,4,6])
        
        #creating a empty list to get all the key values
        Keys=[]

        #creating a empty list to get all the  values
        Values=[]

        #getting all the key values and appending it to list (keys)
        for i in result.keys():
            Keys.append(i)

        #getting all the  values and appending it to list (Values)
        for i in result.values():
            Values.append(i)


        self.assertEqual(len(Keys),len(Values))    

    
    def test_nullValueCheck(self):
        result=Key_Value_dictonary.makeDictonary([1,2,3,5],[2,3,4,6])

        #creating a empty list to get all the key values
        Keys=[]

        #creating a empty list to get all the  values
        Values=[]

        #getting all the key values and appending it to list (keys)
        for i in result.keys():
            Keys.append(i)

        #getting all the  values and appending it to list (Values)
        for i in result.values():
            Values.append(i)

        #checking the length of the key and the value is not null
        if len(Keys)!=0 and len(Values)!=0:
            notNull=True
        else:
            notNull=False

        self.assertEqual(notNull,True)     



if __name__=='__main__':
    unittest.main()