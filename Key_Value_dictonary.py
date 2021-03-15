def makeDictonary(keys , values):
    #printing the keys of first list
    # print("key: ",keys)

    #printing the values of second list
    # print("values:", values)

    #creating an empty dictonary
    Dictonary={}

    #condition to check if keys are more than values put NONE value to last key
    if(len(keys) > len(values)):
        for i in range(0,len(values)):
            Dictonary[keys[i]] = values[i]
    #adding NONE value to the last element of the dictonary key
        for i in range(len(values) , len(keys)):
            Dictonary[keys[i]] = None
    #condition to check if vlues are more than keys remove the extra values       
    if(len(keys) <= len(values)):
        for i in range(0,len(keys)):
            Dictonary[keys[i]] = values[i]
       
    # print("Dictonary is: ",Dictonary)

    #returning the dictonary values
    return Dictonary

print(makeDictonary([1,2,3,4],[2,3,4]))

