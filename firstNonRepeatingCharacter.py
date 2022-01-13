 def firstNonRepeatingCharacter(string):

    dic = {} # create a hash table for counting characters

    lst = list(string) # create a lst with all the characters in the string

    for x in lst:

        dic[x]=dic.get(x,0) + 1 # count the character inside the list

    for index in range(len(lst)):

        x = lst[index]

        if dic[x] == 1:

            return index

    return -1