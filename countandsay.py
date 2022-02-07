def next_number(s):
    #print(s)
    list = []
    count = 1
    for element in range(0,len(s)-1):
       if s[element] == s[element + 1]:
            count += 1
            #print(True)
       else:
           list.append(str(count))
           list.append(s[element])
           count = 1
    list.append(str(count))
    list.append(s[len(s)-1])
    return list



def getting_value(n):
    s = "1"
    for element in range(0, n-1):
        s = next_number(s)
    return "".join(s)
print(getting_value(4))
