# input string, query string.

# #idea
# iterate through the queries - 
# and for each iteration of query, iterate the string --
# and compare each of them and if equal increase the counter until the inner completes and append the counter and initialze the counter to 0

# {"aba":2,"baba""1,"xzzb'':1}

# iterate through my queries and retrieve the value of that particular string and append each time.

def sparearray(strings, query):
    dictionary = {}
    list = []
    for element in strings:
        if element in dictionary:
            dictionary[element] += 1
        else:
            dictionary[element] = 1

    for element in query:
        if element in dictionary:
            list.append(dictionary[element])
        else:
            list.append(0)
    return list
print(sparearray(["aba","xzxb","ab"],[]))





        
