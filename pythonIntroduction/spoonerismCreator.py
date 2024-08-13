def make_spoonerism(word1, word2):
  spoonerism = ""
  aux1= word1[1: len(word1)]
  aux2= word2[1: len(word2)]
  aux = word2[0] + aux1 + " " + word1[0] + aux2
  spoonerism += aux
  return spoonerism
# Uncomment these function calls to test your function:
print(make_spoonerism("Codecademy", "Learn"))
# should print Lodecademy Cearn
print(make_spoonerism("Hello", "world!"))
# should print wello Horld!
print(make_spoonerism("a", "b"))
# should print b a
