def validsudoku(target):
    value = [1,2,3,4,5,6,7,8,9," "]
    for element in target:
        tiger = 0
        count = 0
        for number in element:
            if number not in value or number in element[count+1 :] or number in convert(tiger, count):
                return False
            count += 1
        tiger += 1
    return True

def convert(tiger, count):

    new_list = []
    while tiger < len(target):
        new_list.append(target[][])
        tiger += 1
    return new_list
print(validsudoku([[1,2,3],[5,6,7]]))





    


