# Given a list of Strings representing individual words, count the number of occurrences of all 2-character sequences of letters in those words. For example, suppose the list contains [""banana"", ""bends"", ""i"", ""mend"", ""sandy""]. This list contains the following two-character pairs: ""ba"", ""an"", ""na"", ""an"", ""na"" from ""banana""; ""be"", ""en"", ""nd"", ""ds"" from ""bends""; ""me"", ""en"", ""nd"" from ""mend""; and ""sa"", ""an"", ""nd"", ""dy"" from ""sandy"". 

# (Note that ""i"" is only one character long, so it contains no pairs.) 

# Your method should count the occurrences of these pairs of letters and return the counts as a Map. In this case you would return {an->3, ba->1, be->1, ds->1, dy->1, en->2, me->1, na->2, nd->3, sa->1}. Notice that pairings that occur more than once in the same word should be counted as separate occurrences. For example, ""an"" and ""na"" each occur twice in ""banana"".

# [“banana”, “bends”, “banana”, “i”, “banana”, “mend”, “sandy”]
def strings(list):
    dictionary = {}
    # frequency_dictionary = {}
    # for element in list: 
    #     if element in frequency_dictionary:
    #         frequency_dictionary[element] = frequency_dictionary[element] + 1
    #     else:
    #         frequency_dictionary = 1 

    # The general solution. o(N*m) solution where N is the no of strings in the list and m is the length of the strings -- highest length of the string.
    for element in list:
        count= 2
        if len(element) > 1:
            for value in range(0, len(element)-1):
                pairs = element[value:count]
                # print(value)
                # print(count)
                # print(pairs)
                if pairs in dictionary: 
                    dictionary[pairs] = dictionary[pairs] + 1 # frequency_dictionary[element] 
                else:
                    dictionary[pairs ] =  1#frequency_dictionary[element]  # 3
                count += 1
            
            
    return dictionary

#print(strings(["google", "google", "google"]))


# # What can i optimize??
# suppose all of the strings in the list are same and my above code iterate through the each strings every time.Is it necessary?

# create a dictionary which counts how many times they have repeated and multiply each pairs by that repeatation and once you are done it one time,
# next time you can ignore if you get as same string.

def strings(list):
    dictionary = {}
    frequency_dictionary = {}
    for element in list: 
        if element in frequency_dictionary:
            frequency_dictionary[element] = frequency_dictionary[element] + 1
        else:
            frequency_dictionary[element] = 1 

    
    for element in list:
        count= 2
        if len(element) > 1 and  frequency_dictionary[element] != -1:
            for value in range(0, len(element)-1):
                pairs = element[value:count]
                # print(value)
                # print(count)
                # print(pairs)
                if pairs in dictionary: 
                    # if the pairs is already present, add previous value and the string frequency.
                    dictionary[pairs] = dictionary[pairs] + frequency_dictionary[element] 
                else:
                    # if the pairs is not present in the dictionary then, then add their string repeatation.
                    dictionary[pairs ] =  frequency_dictionary[element]  # 3
                count += 1
            frequency_dictionary[element] = -1
            
        
    return dictionary
print(strings(["google","google"]))
