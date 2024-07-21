letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

letter_to_points = {}
letters.append(" ")
points.append(0)
letter_to_points = dict(zip(letters,points))
print(list(letter_to_points))

def score_word(word):
  point_total = 0
  for letter in word:
    for key, value in letter_to_points.items():
      if letter == key:
        point_total+= value
      else:
        point_total += 0

  return point_total

brownie_points = score_word("BROWNIE")
print(brownie_points)
#(B + R + O + W + N + I + E) -> (3 + 1 + 1 + 4 + 4 + 1 + 1) = 15
