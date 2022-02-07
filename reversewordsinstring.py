def reversewordsinstring(s):
    # First of all, using split function to take all the strings into the list and now we can reverse them and after reversing joining them
    # While joining, if we just say, join, it will join everything in the list so we say join when you get a space so keeping a space infron in'
    # the join function . so this will help us to get the correct answer.
    list = []
    list = s.split()
    start = 0
    end = len(list)-1
    print(list)
    while start < end:
        temp = list[start]
        list[start] = list[end]
        list[end] = temp
        start += 1
        end -= 1
    print(list)
    return " ".join(list)
print(reversewordsinstring("The weather is amazing today!"))
