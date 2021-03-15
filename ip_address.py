# importing the module
import re
import os

def IpAddressFetch(filename):

    # getting the current working directory
    path=os.getcwd()

    # opening and reading the file 
    with open(f'{path}/{filename}') as log:
        String = log.readlines()

    #regular expression for the ip address 
    RegexIpPattern = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')

    #creating an empty Ip address list to append the ip address
    IpAddressList=[]

    #extracting all the ip address and appending into list 
    for IpList in String:
        IpAddressList.append(RegexIpPattern.search(IpList)[0])


    #creating an empty dictonary 
    frequency = {}

    #adding the ip list and its frequency of occurance in the frequency dictonary
    for Counter in IpAddressList:
        if Counter in frequency:
            frequency[Counter] = frequency[Counter] + 1
        else:
            frequency[Counter] = 1
    
    #getting the sorted ip list in descending order
    Sorted_Ip_list=sorted(frequency.items(), key=lambda x: x[1], reverse=True)


    #values of top ten ip list with its frequency
    Sorted_Ip_list_Ten_values=Sorted_Ip_list[:10]

    #creating an empty list to append the top ten ip list 
    Top_Ten_Ip_list=[]

    #appending the IP values to the empty list created 
    for i in range(len(Sorted_Ip_list_Ten_values)):
        Top_Ten_Ip_list.append(Sorted_Ip_list_Ten_values[i][0])

    return Top_Ten_Ip_list

print(IpAddressFetch('access.log'))