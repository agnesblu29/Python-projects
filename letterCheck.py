def letter_check(word, letter):
  counter = 0
  for i in word:
    if(i==letter):
      counter +=1
    
  if counter > 0:
      return True
  else:
      return False
  

print(letter_check("apple", "e"))
