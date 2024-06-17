destinations = [["Paris, France"], ["Shanghai, China"], ["Los Angeles, USA"], ["São Paulo, Brazil"], ["Cairo, Egypt"]]

test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]

attractions = [[], [], [], []]

def get_destination_index(destination):
  i=0
  while(destinations[i].count(destination) == 0):
     i= i+1
  
  destination_index=i
  return destination_index

def get_traveler_location(traveler):
  traveler_destination = traveler[1]
  traveler_destination_index = get_destination_index(traveler_destination)
  return traveler_destination_index

def add_attraction(destination, attraction):
  destination_index = get_destination_index(destination)

print(get_destination_index("Los Angeles, USA"))
print(get_destination_index("Paris, France"))
test_destination_index = get_traveler_location(test_traveler)
print(test_destination_index)
print(attractions)
