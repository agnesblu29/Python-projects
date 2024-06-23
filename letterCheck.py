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

def contains(big_string, little_string):
  return little_string in big_string

def common_letters(string_one, string_two):
  list_lettersInCommon = []
  for j in string_one:
      if (j in string_two) and not(j in list_lettersInCommon):
        list_lettersInCommon.append(j)
  return list_lettersInCommon


print(contains("watermelon", "melon"))
print(common_letters("banana", "cream"))
