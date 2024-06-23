authors = "Audre Lorde,Gabriela Mistral,Jean Toomer,An Qi,Walt Whitman,Shel Silverstein,Carmen Boullosa,Kamala Suraiyya,Langston Hughes,Adrienne Rich,Nikki Giovanni"

print(authors)
author_names = authors.split(",")
print(author_names)
author_last_names = []
aux= []
for i in author_names:
  aux = i.split(" ")
  author_last_names.append(aux[-1])

print(author_last_names)
