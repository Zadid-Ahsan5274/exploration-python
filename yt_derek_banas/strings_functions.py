rand_string = "    this is an important string    "
rand_string = rand_string.lstrip()
rand_string = rand_string.rstrip()
rand_string = rand_string.strip()

print(rand_string.capitalize())
print(rand_string.upper())
print(rand_string.lower())

a_list = ["Bunch","off","random","words"]
print(" ".join(a_list))

a_list_2 = rand_string.split()
for i in a_list_2:
    print(i,end=" ")
print()
print("How many is: ",rand_string.count("is"))
print("Where is string: ",rand_string.find("string"))
print(rand_string.replace("an","a kind of"))

'''
original_string = input("Enter original string: ")
original_string = original_string.upper()
list_of_words = original_string.split()
for word in list_of_words:
    print(word[0],end="")
print()
'''
letter_z = "z"
num_3 = "3.14"
a_space = " "
'''print("Is z a letter or a number: ",letter_z.isalnum())
print("Is z a letter: ",letter_z.isalpha())
print("Is 3 a number: ",num_3.isdigit())
print("Is z a lower: ",letter_z.islower())
print("Is z a upper: ",letter_z.isupper())
print("Is space a space: ",a_space.isspace())'''

def is_float(str_val):
    try:
        float(str_val)
        return True
    except ValueError:
        return False

print("Is PI a float: ",is_float(num_3))

message = input("Enter your message: ")
key = int(input("How many characters should we shift (1-26): "))
secret_message = ""
for char in message:
    if char.isalpha():
        char_code = ord(char)
        char_code += key

        if char.isupper():
            if char_code > ord('Z'):
                char_code -= 26
            if char_code < ord('A'):
                char_code += 26
        else:
            if char_code > ord('Z'):
                char_code -= 26
            if char_code < ord('A'):
                char_code += 26
        secret_message = secret_message + chr(char_code)
    else:
        secret_message = secret_message + char

print("Encrypted: ",secret_message)

key = -key
original_message = ""

for char in secret_message:
    if char.isalpha():
        char_code = ord(char)
        char_code += key

        if char.isupper():
            if char_code > ord('Z'):
                char_code -= 26
            if char_code < ord('A'):
                char_code += 26
        else:
            if char_code > ord('Z'):
                char_code -= 26
            if char_code < ord('A'):
                char_code += 26
        original_message = secret_message + chr(char_code)
    else:
        original_message = secret_message + char

print("Decrypted: ",original_message)

