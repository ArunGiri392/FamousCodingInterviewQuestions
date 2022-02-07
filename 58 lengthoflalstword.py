# Input: s = "Hello World"
# Output: 5
# Explanation: The last word is "World" with length 5.

# Input: s = "   fly me   to   the moon  "
# Output: 4
# Explanation: The last word is "moon" with length 4.

# s = "" -- There will be a word
# s = "arun" -- arun
# s = "    " == THis will not occur.
# s consists of only English letters and spaces ' '.
# a-z, " "
#  "i       am          " -- 'am'

#  1) if it is a last word, then there will not be any letter after that and there might be spaces which i can ignore.

#  to through the entire string and if i find space then it means that the word is completed and if i find any letter, then this is not the last word and andagain
#  iterate.

# 2) loop from the back and if there is a space just ignore it and go on and when you find letter put them into the list until you find another space.

# 3) if i find any spaces before i find letters, ignore it but if i find any space after i find any letters. break the loop.LookupError


# "   fly me   to   the moon  "

# # for loop 
# #  "Hello World"
# "microsoft"

def lengthoflastword(strings):
    result = []
    for element in range(len(strings)-1, -1,-1):
        if len(result) == 0 and strings[element] == " ":
            continue
        elif strings[element] == " " and len(result) > 0:
            break
        else:
            result.append(strings[element])
    return len(result)
    
print(lengthoflastword("luffy is still joyboy"))





