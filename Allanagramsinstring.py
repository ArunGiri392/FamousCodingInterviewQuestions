def allanagrams(s,p):
    dictionary1 = {}
    for element in p:
        if element in dictionary1:
            dictionary1[element] += 1

        else:
            dictionary1[element] = 1
    print(dictionary1)
    print()
    dictionary2 = {}
    for element in range(0,len(p)):
        if s[element] in dictionary2:
            dictionary2[s[element]] += 1

        else:
            dictionary2[s[element]] = 1
    print(dictionary2)
    list = []
   

    
    for element in range(0, len(s)-len(p)):
        if dictionary1 == dictionary2:
            list.append(element)


        if dictionary2[s[element]] == 1:
            dictionary2.pop(s[element])
        else:
             dictionary2[s[element]] -= 1

        if s[element + len(p)] in dictionary2:
            dictionary2[s[element + len(p)]] += 1
        else:
            dictionary2[s[element + len(p)]] = 1
        #print(element)
        print(dictionary2)
        # if dictionary1 == dictionary2:
        #     list.append(element)
        # if dictionary1 == dictionary2:
        #     list.append(element)

        # if dictionary1 == dictionary2:
        #     print(True)
        #     list.append(element)
        #     print(dictionary2)
    if dictionary1 == dictionary2:
            list.append(element+1)

    return list
print(allanagrams("cbaebabacd","abc"))


        
