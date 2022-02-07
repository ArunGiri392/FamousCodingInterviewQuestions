def is_alphanumeric(c):
        if c.isalnum() == True:
            return True
        return False

def palindrome(s):
    start = 0
    end = len(s) - 1
    s = s.lower()
    

    while start < end:
        is_start_alphanum =  is_alphanumeric(s[start])
        is_end_alphanum =  is_alphanumeric(s[end])
        if is_start_alphanum  !=  True:
          start += 1  
        if is_end_alphanum!= True:
          end -= 1
        print(s[start])
        print(s[end])
       
 
        if is_start_alphanum == True and is_end_alphanum == True:
            if s[start] != s[end]:
                return False
        
            start += 1
            end -= 1
    return True
#print(palindrome("A man, a plan, a canal: Panama"))

def isPalindrome(self, s):
        start = 0
        end = len(s) - 1
        s = s.lower()


        while start < end:
            if is_alphanumeric(s[start]) == False:
                start += 1
                continue
            if is_alphanumeric(s[end]) == False:
                end -= 1
                continue
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True

def is_alphanumeric(c):
        if c.isalnum() == True:
            return True
        return False
#print(palindrome("A man, a plan, a canal: Panama"))

# how to use is_alnum.
def alnum(s):
  if s.isalnum() == True:
    return True
  return False
print(alnum("&"))
