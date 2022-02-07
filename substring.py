#Write a function that takes in two strings and returns true if the second string is substring of the first , and false otherwise.
 #umpire
#  continous or without
#  uppercase and lowercase  -- edge case
#  empty String  -- edge case
# same letters -- edge case
# edge cases.
# "cat" -- "catastrophic" -- False
# "cat" -- "" -- True
# "aaaa" -- "aaa"
# " " -- " "

# 1) in operator to check if the second string is present in first string or not.


# 2)  FIRST OF ALL, CHECK IF THE FIRST ELEMENT OF 2ND STRING IS IN 1ST OR NOT, IF NOT RETURN FALSE.
# WITH TWO VAI=RIABLES KEEP TRACK AND INCREMENT BOTH IF THE LETTER MATCHES AND IF DOES NOT MATCHES JSUT INCREMENT I AND KEEP J 0 BECAUSE WE WANT TO ALWASY 
#CHECK FROM FIRST.
# AT LAST. IF MATCHED, WE KNOW THAT J IS EQUAL TO THE LENGTH OF SECOND STRING, IF NOT, WE KNOW THERE IS NO SUBSTRING.



def substring(first_string, second_string):
    if second_string in first_string:
        return True
    return False
#print(substring("arun","ar"))

def substring1(first_string, second_string):
    if second_string[0] not in first_string:
        return False
    i = 0 
    j = 0
    while i < len(first_string) and j < len(second_string):
        if first_string[i].lower() == second_string[j].lower():
            i += 1
            j += 1
        else:
            i += 1
            #j = 0
            
        
        
    
    if j == len(second_string):
        return True
    return False
        
print(substring1("mississippi","issip"))
# Time complexity = o(N)
#Space complexity = 0(1)

def substring(str1, str2):
  left_pointer_1 = 0  # points to str1
  left_pointer_2 = 0  # points to str2
  '''
  assuming the problem is NOT case sensitive and account for cases
  Input: baby, BABY
  Output: true  
  '''
  str1 = str1.lower() 
  str2 = str2.lower()

  #using 2 pointers to go through each character in str1 and str2
  #and check if they match
  while left_pointer_1 < len(str1) and left_pointer_2 < len(str2):
    if str1[left_pointer_1] == str2[left_pointer_2]:
      left_pointer_2 += 1
    left_pointer_1 += 1

  return left_pointer_2 == len(str2)

print(substring("mississippi","issipi"))


# order does not matter in this soluiton.

