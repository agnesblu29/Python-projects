starting_money = 100
starting_num_items = 10
item_price = 4

# Your code here
def buy_items(starting_money,starting_num_items,item_price):
  num_bought = 0
  total_bought = 0
  while(True):
      aux= total_bought + item_price
      starting_num_items -= 1
      if (aux <= starting_money and starting_num_items >= 0):
        total_bought = total_bought + item_price
        num_bought +=1
        #print(total_bought)
        
      else:
        break
        
  return num_bought

total = buy_items(starting_money, starting_num_items, item_price)
print("You were able to buy " + str(total) + " items.")
  
# For testing purposes
total_1 = buy_items(100, 10, 4)
print("Test 1: " + str(total_1))
total_2 = buy_items(10, 10, 4)
print("Test 2: " + str(total_2))
