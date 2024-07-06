#Our store makes sure all discounted items have odd prices while normal items have even prices.Find all items with an odd price and add the name of the item to the discounted_items list.#

# All of our store items
all_items = [["Taffy", 1], ["Chocolate", 2], ["Cup", 5], ["Plate", 10], ["Bowl", 11], ["Silverware", 22]]

# Empty discounted_items list
discounted_items = []

# Your code here
for item in all_items:
  for element in item:
    if type(element)== int and not(element % 2 == 0):
      discounted_items.append(item[0])

      
# For testing purposes: print discounted list
print(discounted_items)


