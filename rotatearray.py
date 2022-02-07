
# from abc import abstractproperty


# 1 2 3 4 5  k = 2

# 4 5 1 2 3
# first reverse the array 
# 5 4 3 2 1
# and reverse the k first elements and reverse the remaining part.
# 4 5 1 2 3

# The helper function reverses the array based on the list, start and end value provided.So,each time we call the helper function with 
# different start, end .
# Also repeating 6 times is same as repeating 1 times so if k is greater than len(list) then we find the remainder and update the k.


def helper_function(list,start, end):
  while start < end:
    temp = list[start]
    list[start] = list[end]
    list[end] = temp
    start += 1
    end -= 1

def rotate(list,k):
  if k > len(list):
    k = k % len(list)
  start = 0
  end = len(list) - 1
  helper_function(list,start,end)

  start = 0
  end = k - 1
  helper_function(list,start,end)

  start = k
  end = len(list)-1
  helper_function(list,start,end)
  return(list)
  
print(rotate([1,2,3,4,5],6))


 
  
   
  




def rotatesinglearray(list):
  #only rotating the array by 1.
  temp = list[0]
  count = list[1]
  for i in range(0,len(list)-2):
    #  if i == len(list) - 2:
    #    count == list[len(list)-1] # last element
    #  if i == len(list) - 1:
    #   list[0] = count
      #return list
    list[i+1] = temp
    temp = count
    count = list[i+2]
  #print(i)
  print(temp)
  print(count)
  list[len(list)-1] = temp
  list[0] =count
  return list
#print(rotatesinglearray([1,2,3,4,5,6,7,8]))




   

# using an additional space.just create a array with all zero and place all the other elements
# from the array in respective postions.
def rotate_array(list):
  value = len(list)
  two_list = []
  for element in range(0, len(list)):
    value = []
    for result in range(0,len(list)):
      value.append(0)
    two_list.append(value)
  
  for element in range(0,len(list)):
    for value in range(0,len(list)):
      two_list[element][value] = list[len(list)-1-value][element]
  return two_list

  
#print(two_array([[1,2,3],[4,5,6],[7,8,9]]))
# TIme complexity = 0(M * N) where M is the number of rows and N is the no of columns.
#space complexity = o(M * N) Where M is the number of rows and N is the number of columns.

# Also can be said Time complexity  as O(N) where N is the total no of elements in the list.

# Pattern -- 00 -- 30
#            01 -- 20
#            02 -- 10
#            03 -- 00
#            ie [element][value] = [len(list)-1-value][element]
#In place solutions.
#   1 2 3      1 4 7     7 4 1
#   4 5 6      2 5 8 --  8 5 2
#   7 8 9   -- 3 6 9     9 6 3
#   First transposing the matrix and then swapping the elements until we reach the middle of matrix.
# Transposing. matrix[i][j] = matrix [j][i]
def rotatearray(matrix):
  for row in range(0, len(matrix)):
    #print(str(row) + "i am row")
    for col in range(row,len(matrix)):
      #This loop should start from row. if starts from 0 then double swapping will occur and 
      #we will not be able to swap becuase we just want to swap them once.NOt twice.
      
      #print(str(col) + "i am column")
      temp = matrix[row][col]
     
      matrix[row][col] = matrix[col][row]
      matrix[col][row] = temp
    
  #swapping the matrix so that it gets rotated.
  # pattern for swapping.
  # after transposing the matrix we get:
  # let us suppose we have 4*4 matrix so 
  # original = 
  # 1 2   3   4
  # 5 6   7   8
  # 9 10 11  12
  # 13 14 15 15
  # after tranposing it becomes:

  # 1 5 9  13 
  # 2 6 10 14
  # 3 7 11 15
  # 4 8 12 16
  # now we see that if we are just able to swap first and last and 2nd and 2nd last in row,the 
  # matrix is resulted so.len(matrix)//2 is done because we just want to swap the row up to half
  for row in range(0, int(len(matrix)/2)):
    for col in range(0, len(matrix)):
      temp = matrix[col][row]
      matrix[col][row] = matrix[col][len(matrix)-1-row]
      matrix[col][len(matrix)-1-row] = temp
  return matrix


  

#print(rotatearray([[1]]))
  
