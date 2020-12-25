fname = input("first name : ")
lname = input("last name : ")
age = int(input("Age"))
data = int(input("Data of birtday (just year) : "))

userlist = [fname, lname, age, data]

for i in (userlist):
    print(i)

if age < 18:
    print("You can't go out because it's too dangerous")
else:
    print("you can go out to the street")
