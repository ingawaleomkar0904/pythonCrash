
text = " Enginerring"
print(text.lstrip()) # Removes leading whitespace

text = "Enginerring "
print(text.rstrip()) # Removes trailing whitespace

text = " Enginerring "
print(text.strip()) # Removes leading and trailing whitespace

text = "#### Enginerring ###".strip("#") # Removes leading and trailing '#' characters
print(text)


text = "Data Enginerring"
print(f"Length of the string: {len(text)}")
print(f"Length of the string after stripping: {len(text.strip(" "))}")


messy_str = " 968-Maria, ( D@t@ Engineer );; 27y  " # Input string 
#Output--> name: Maria | role: Data Engineer | age: 27

messy_str = messy_str.strip() # Remove leading and trailing whitespace
print(f"Messy String = {messy_str}")
print(f"Length of messy String = {len(messy_str)}") 
name = messy_str.split('-')[1].strip() # Split the string at '-' and remove leading and trailing whitespace

print(f"Name: {name} \n" + name.replace("@","a"))
role = messy_str.split(";")[1].strip()
age = messy_str.split(";")[2].strip()

print(f"Role: {role}")
print(f"Age: {age}")
#------------------------------------------------------------------------------------


row = "23, 7.5, True"

age, price, flag = row.split(",")

print(f"Age: {age}, Price: {price}, Flag: {flag}")

