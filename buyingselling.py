def buyingselling(list):
    max = 0
    
    for element in range(len(list)):
        for value in range(element + 1, len(list)):
            if list[element] < list[value]:
                result = list[value] - list[element]
                if result > max:
                    max = result
                    buy = element
                    sell = value
    print(" i am profit {}".format(max))
    print(buy)
    print(sell)
print(buyingselling([310,315,275,295,260,270,290,230,255,250]))

#Time complexity = O(N^2)
#space complexity =o(1)

# idea 2
# reduced complexity
# 310, 315, 275, 295, 260, 270, 290, 230, 255, 250
# min  5    min  20   min   10  30   min  25   min

# We keep track of the minimum value we have encountered so far and we when we get the number greater than the minimum value we subtract them to get a 
# maximum profit. If the next number is smaller than the previous minimum number, we keep the number as the new minimum number.We also keep track of 
# the highest profit every time and we return it at the end.

# pseudocode
# if element is greater than min - calculate the profit and update the max profit 
# else:
#   update minimum
# return the max profit

def buy_and_sell_stock_once(list):
  minimum = list[0]
  max_profit = 0
  profit = 0
  for element in range(1, len(list)):
    if list[element] > minimum:
      profit = list[element] - minimum
      max_profit = max(max_profit,profit)
    else:
      minimum = list[element]
  return max_profit
#print(buy_and_sell_stock_once([310, 315, 275, 295, 260, 270, 290, 230, 255, 250]))
# 
# # min = 2
# profit = 290 - 255 = 25
# max_profit = max(30, 25 )  = 30
# element = 260





