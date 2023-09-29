#محمد ناصر عبدالوهاب
#1

name = input("Enter your Name : ")
age = input("Enter your age : ")
street = input("Enter your street : ")
city = input("Enter your city : ")
country = input("Enter your country : ")

#2

print(f"\" your Name : {name} \"")
print(f"\" your age : {age} \"")
print(f"\" Address : {street}, {city}, {country} \"\n")

#3

new_age = int(age) - 5
print(f"\" Hello {name} Your age is Years {new_age} Old, Your Address is {street}, {city}, {country} \"\n")

#4

print(type(name))
print(type(age))
print(type(street))
print(type(city))
print(type(country))
print("\n")

#5

print(f"Hello {name}," + " How Are You? \ \"\"\" " + "Your Age Is ? " + f"\"{new_age}\"" + f" And Your Country Is: {country}\n\n")

#6

print(f"Hello {name}," + " How Are You? \ \n \"\"\" " + "Your Age Is ? " + f"\"{new_age}\"" + f" And \n Your city Is: {city}\n")

#7

Name = 'ITF Gsg Python'
print("First Letter Is : " + Name[0])
print("Third Letter Is : " + Name[2])
print("Last Letter Is : " + Name[13] +"\n")
#8
print(Name[11:14])
print(Name[0:3])
print(Name[13:7:-1]+"\n")

#9

Var = "$&$&Mohammed$&$&"
Var1 = Var.strip("$&")
print(Var1, "\n")

#10

msg = "I %7 Python And Although I %7 GSG with Zakaria"
masg1 = msg.replace("%7", "Love")
print(masg1 + "\n")

#11

num1 = "4"
num2 = "56"
num3 = "963"
num4 = "385"
num5 = "8719"
num6 = "87190"

#12

print(f"{num1.zfill(5)}")
print(f"{num2.zfill(5)}")
print(f"{num3.zfill(5)}")
print(f"{num4.zfill(5)}")
print(f"{num5.zfill(5)}")
print(f"{num6.zfill(5)}")

#13

#The merhod (title) {there are used to manipulate the capitalization of strings}
first_name = "MOHAMMED"
last_name = first_name.title()
print("\n", last_name)
#The method (capitalize) {capitalizes only the first character of the string}
full_name = "mohammed nasser abdel wahab"
full_name_1= full_name.capitalize()
print(full_name_1, "\n")

#14

my_txt = "Mohammed"
print("*" * 11 + my_txt)
print("*" * 11 + my_txt + "*" * 11)
print(my_txt + "*" * 11)

#15

name_one = "SaMER"
name_two = "Abed"
print("\n", name_one.swapcase())
print(name_two.swapcase())
print(name_one.lower())
print(name_two.upper(), "\n")

#16

print(name_one.isupper())
print(name_two.islower(), "\n")

# ** Bouns **
#17

#name_one
if name_one[0] == 'S':
    print("name_one starts with 'S'")
else:
    print("name_one does not start with 'S'")

#name _two

if name_two[2:4] == 'HD':
    print("name_one starts with 'HD'")
else:
    print("name_one does not start with 'HD' \n")

#18


msg_tow= "I Love Python And Although I Love GSG with Zakaria"
love_count = msg_tow.count("Love")
t_count = msg_tow.count("t")
print("Number of <Love> is : ", love_count)
print("Number of <t> is : ", t_count, "\n")

#19

msg_Third = "I %7 Python And Although I %7 GSG with Zakaria"
new_msg = msg_Third.replace("%7", "Love", 1)
print(new_msg, "\n")

#20

test1 = "ZakZak"
test2 = "Zakaria"
test3 = "A war at Tarawa"
test4 = "madam"

#test1
if (test1[:3] == test1[3:]):
    print("ZakZak is symmetrical ")
else:
    print("ZakZak is NOT symmetrical")
if (test1[:3] == test1[5:2:-1]):
    print("and ZakZak is a palindrome")
else:
    print("but ZakZak is NOT a palindrome\n")



#test2
if (test2[:3] == test2[3:]):
    print("Zakaria is symmetrical")
else:
    print("Zakaria is NOT symmetrical")
if (test2[:3] == test2[6:2:-1]):
    print("Zakaria is a palindrome")
else:
    print("and Zakaria is NOT a palindrome\n")



#test3
if (test3[:8] == test3[8:]):
    print("A war at Tarawa. is symmetrical")
else:
    print("A war at Tarawa. is NOT symmetrical")

if ((test3[:8].lower().replace(" ", "")) == (test3[-1:8:-1].lower().replace(" ", ""))):
    print("but A war at Tarawa. is a palindrome\n")
else:
    print("but A war at Tarawa. is NOT a palindrome")



#test4
if (test4[:2] == test4[2:]):
    print("madam is symmetrical")
else:
    print("madam is NOT symmetrical")

if (test4[:2] == test4[4:2:-1]):
    print("but madam is a palindrome")
else:
    print("but madam is NOT a palindrome")