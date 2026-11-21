user_name = "Omkar"
age = 14

print(f"My name is {user_name} and my age is {age}")  # My name is Omkar and my age is 34

if user_name is not None and user_name != "":
    print(f"User name is {user_name}")  # User name is not empty
else:
    print("User name is empty")  # User name is empty


if age > 18:
    print(f"{user_name} is an adult")  # Omkar is an adult
else:
    print(f"{user_name} is not an adult")  # Omkar is not an adult

# #------------------------------------------------------------------------------------------------------------------

password = "Linux@#$0904"

if len(password) >= 8 and any(char.isdigit() for char in password) and any(char.isupper() for char in password) and any(char.islower() for char in password) and any(not char.isalnum() for char in password):
    print("Password is strong")  # Password is strong
else:
    print("Password is weak")  # Password is weak
# #------------------------------------------------------------------------------------------------------------------

email = "omkar.ingawale@hotmail.com"

#if email !="" and "@".count("email")==1 and email.endswith(".com") and len(email)<=254:
if email != "" and email.count("@") == 1 and email.endswith(".com") and len(email) <= 254:
    print(f"{email} is valid email address")  # omkar.ingawale@hotmail.com is valid email address

# if email!= "" and "@" in email and ".com" in email:
#     print(f"{email} is valid email address")
# else:
#     print(f"{email} is not a valid email Id")
#------------------------------------------------------------------------------------------------------------------

userName = "Omkar"

print(userName!= None and isinstance(userName, str) and len(userName) >=5)  # True
#------------------------------------------------------------------------------------------------------------------