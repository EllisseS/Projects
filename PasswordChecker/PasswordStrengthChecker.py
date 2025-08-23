#!/user/bin.env python3
"""
--- Version 1 : 8/22/2025 ---
"""
import string

print("Password Strenght Checker")

user_pass = input("Enter Password: ")
pass_count = len(user_pass)
num_check = any(char.isdigit() for char in user_pass)
special_check = any(char in string.punctuation for char in user_pass)
has_upper = any(char.isupper() for char in user_pass)

with open("passwordlist.txt", "r") as file:
  found = False
  for line in file:
    if user_pass == line.strip():
      found = True
      break

if found:
  print("Password was found in a common password list. Don't use it!")
else:
  if (pass_count >= 16):
    if(num_check is True  and special_check is True and has_upper is True):
      print("Strong Password, has at least one number and special character good job!")
    elif(num_check is True and special_check is True and has_upper is False):
      print("Medium Password: You just need an uppercase letter")
    elif (num_check is True and special_check is False and has_upper is True):
      print("Medium Password: Almost there, needs at least one special character")
    elif(num_check is False and special_check is True and has_upper is True):
      print("Medium Password: So close! need at least one number")
    elif(num_check is False and special_check is True and has_upper is False):
      print("Weak Password: Missing number and upper case letter")
    elif(num_check is False and special_check is False and has_upper is True):
      print("Weak Password: Need number and special character")
    elif (num_check is True and special_check is False and has_upper is False):
      print("Weak Password: Missing uppercase letter and special character")        
    else:
      print("Very Weak Password! Add some uppercase letters, numbers, and even a special character")
  else:
    print("Password Length Needs Improvement. Don't use password this password")
