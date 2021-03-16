import re 


def PasswordValidationWithRules(password):

    #creating an empty list to validate the password 
    flag = []

    # first checking for the length if it is between 1 to 20 characters
    if(len(password)>=1 and len(password)<=20 

    # then validating the first character of password if it is a latin letter
    and (re.search("[A-Z]", password[0]) or re.search("[a-z]", password[0]) ) 

    #then validating the last letter of password  if it is in latin letters or numbers 
    and (re.search("[A-Z]", password[len(password)-1]) or re.search("[a-z]", password[len(password)-1]) 
    or re.search("[0-9]", password[len(password)-1]))): 

        flag.append(1)
    
    else:
        flag.append(0)

    #now checking for remaining letter between first and last
    for values in range(1,len(password)-1):

        #if it is in latin letters or numbers or dot or minus symbol
        if (re.search("[A-Z]", password[values]) 
        or re.search("[1-9]", password[values]) 
        or re.search("[a-z]", password[values]) 
        or re.search("[.]", password[values]) 
        or re.search("-", password[values])):

            flag.append(1)
        
        else:
            flag.append(0)

    #validating if the password is correct or not
    if sum(flag)==len(password)-1:

        print("valid password")
    else:

        print("invalid password")


def PasswordValidationWithRegex(password):

    #first letter can be alphabet and the last letter can be alphanumeric and the middle elements can be alphanumeric , dot or minus
    RegularExpression="^[a-zA-Z]{1}[a-zA-Z0-9.-]{1,19}[a-zA-Z0-9]$"

    #regular expression is compiled
    MatchingPattern = re.compile(RegularExpression)

    #searching for the regex pattern in the password
    Result = re.search(MatchingPattern, password)

    #validating if password is valid or not 
    if Result:
        print("Valid Password")
    else:
        print("Invalid Password")


PasswordValidationWithRules('a-ba.shj')
PasswordValidationWithRegex('a-ba.sh-1ba.sh-1')