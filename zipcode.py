def zip(list):
  if list == []:
      return ""
  Max = 0
  current = 0
  for value in list:
     current = len(value)
     if current > Max:
         Max = current
  #print(Max)
  result = ""
  for index in range(0, Max):
      for element in list:
          if index >= len(element):
              continue
          result += element[index]
  return result
print(zip(["aayushhhhhhhhhh","abhikkkkkkkkkkkkkkkkkk","sandesh","amnmbmbkbkbi"]))


# Time complexity = O(N^2)
# Space complexity = O(N)


