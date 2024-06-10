weight = 41.5
cost = 0
#Ground shipping
# the cost of ground shipping. It should check for weight, and print the cost of shipping a package of that weight.
if weight <= 2 :
  cost = weight*1.5 +20
elif (weight>2 and weight<=6):
  cost = weight*3 +20
elif (weight>6 and weight<=10):
  cost = weight*4 +20
else:
  cost= weight*4.75 +20

print("Ground Cost of the package:\n",cost)

#Ground shipping premium has a flat charge of 125$
premium_cost = 125
print("Ground Premium Cost of the package:\n",premium_cost)

#Drone Shipping
drone_cost = 0
if weight <= 2 :
  drone_cost = weight*4.5
elif (weight>2 and weight<=6):
  drone_cost = weight*9
elif (weight>6 and weight<=10):
  drone_cost = weight*12
else:
  drone_cost= weight*14.25 

print("Drone Shipping Cost of the package:\n", float(drone_cost))
