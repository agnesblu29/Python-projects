class Node:
  def __init__(self, value, link_node=None):
    self.value = value
    self.link_node = link_node
    
  def set_link_node(self, link_node):
    self.link_node = link_node
    
  def get_link_node(self):
    return self.link_node
  
  def get_value(self):
    return self.value

# instantiate three nodes yacko, wacko and dot
yacko = Node("likes to yak")
wacko = Node("has a penchant for hoarding snacks")
dot = Node("enjoys spending time in movie lots")

#give yacko a link_node to dot
yacko.set_link_node(dot)

#give dot a link_node to wacko
dot.set_link_node(wacko)

#get dot's value from yacko
dots_data = yacko.get_link_node().get_value()
print(dots_data)

#get wacko's value from dot
wackos_data = dot.get_link_node().get_value()
print(wackos_data)
