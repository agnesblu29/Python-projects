def username_generator(first_name, second_name):
  user_name = []
  if (len(first_name) < 3 or len(second_name)<4):
    user_name = first_name + second_name
  else:
    user_name = first_name[0:3] + second_name[0:4]
  return user_name

def password_generator(user_name):
  password = []
  password = user_name[-1] + user_name[:-1]

  return password



username = username_generator("Abe", "Simpson")
print(username)
temporary_password = password_generator(username)
print(temporary_password)
