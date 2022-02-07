def swapping_vowels(s):
    vowel = set("aeiouAEIOU")
    list = []
    for character in s:
      list .append(character)
    

    start = 0
    end = len(s) - 1

    while start < end:
        
        if list[start] not in vowel:
            start += 1
        if list[end] not in vowel:
            end -= 1
        elif list[start] in vowel and list[end] in vowel:
            temp = list[start]
        list[start] = list[end]
        list [end] = temp
        start += 1
        end -= 1

        This was my initial code. Lots of 
        
        
        


        if list[start] not in vowel:
            start += 1
            continue
        if list[end] not in vowel:
            end -= 1
            continue
       
        temp = list[start]
        list[start] = list[end]
        list [end] = temp
        start += 1
        end -= 1
    return "".join(list)
    

print(swapping_vowels("TiGEr"))
