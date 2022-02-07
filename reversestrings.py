from stack import Stack
def reversestrings(string):
    s = Stack()
    for element in string:
        s.push(element)
    reversestring = ""
    while s.is_empty() == False:
        reversestring = reversestring + s.pop()
    return reversestring
print(reversestrings("arun"))
    
def convert_int_to_bin(dec_num):
    s = Stack()
    if dec_num == 0:
        return 0
    while dec_num > 0:
        s.push(dec_num % 2)
        print(dec_num % 2)
        dec_num = dec_num // 2
        print(dec_num)
    binary = ""
    while s.is_empty() == False:
              binary = binary + str(s.pop())
    return binary
          
print(convert_int_to_bin(0))

  


