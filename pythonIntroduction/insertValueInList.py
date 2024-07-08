colors = ['red', 'orange', 'yellow', 'blue', 'indigo', 'violet']

aux= []

for i in colors:
  if i == 'yellow':
    aux.append('yellow')
    aux.append('green')
  else:
    aux.append(i)

colors = aux
print(colors)
