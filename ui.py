print("Create a new account!")
user_first_name = input("First name:  ")
user_surname = input("Surname name:  ")
user_id = input("ID name:  ")
user_pass = input("Set a password:  ")
pass_check = input("Rewrite password:  ")

if user_pass == pass_check:
  print("Congratulation you have created a new account!")
else:
  print("Please write again the password!")
  pass_check = input("Rewrite password:  ")
  if pass_check == user_pass:
    print("Congratulation you have created a new account!")


print("Sign in:")
user_id_ask = input("ID name:  ")
user_pass_ask = input("Password:  ")

while user_id_ask != user_id and user_pass_ask != user_pass:
  if user_id == user_pass_ask or user_pass == user_pass_ask:
    print("wrong ID or password")
    user_id_ask = input("ID name:  ")
    user_pass_ask = input("Password:  ")
  else:
    print("wrong ID or password")
    user_id_ask = input("ID name:  ")
    user_pass_ask = input("Password:  ")

print("Hello " + user_first_name + " " + user_surname + "!")
