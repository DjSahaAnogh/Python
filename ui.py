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
    print("Congratulation you have created a new account!\n")


print("Sign in:")
user_id_ask = input("ID name:  ")
user_pass_ask = input("Password:  ")

if user_id_ask == user_id:
  if user_pass_ask == user_pass:
    print("Hello " + user_first_name + " " + user_surname + "!")
