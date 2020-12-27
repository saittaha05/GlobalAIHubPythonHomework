name = "Sait"
surname = "Şahin"


enterednumber = 3
while True:
    enteredname = str(input("Enter your name : "))
    enteredsurname = str(input("Enter your surname : "))
    if name == enteredname and surname == enteredsurname:
        print(f"Welcome {name} {surname}")
        lessons=["SOCİAL STUDİES","ENGLISH","MATH","HISTORY","MUSIC"]
        chosencourse=[]
        lessonnumber=int(input("How many lessons do you take (You can take a minimum of 3 and a maximum of 5 courses!) :"))
        if 3<=lessonnumber<=5:
            print(f'Lessons you took -> {lessons}')
            while lessonnumber>0:
                coursename=str(input("Enter the name of the lesson :")).upper()
                if coursename not in lessons:
                    print("There is no such course! Type again")
                    lessonnumber += 1
                else:
                    if coursename in chosencourse:
                        print("I remember this letter before. Please guess another letter.")
                        continue
                    chosencourse.append(coursename)
                    print("Registration has been successfully added to your courses...")
                lessonnumber -= 1
            print(f"List of courses you have selected -> {chosencourse}")
            examlesson=str(input("Which course will you take the exam from? :")).upper()
            examgrade={}
            midtermgrade=int(input(f"{examlesson} enter the grade you got from the midterm exam : "))
            finalgrade=int(input(f"{examlesson} enter the grade you got from the final exam : "))
            projectgrade=int(input(f"{examlesson} enter the grade you got from the project exam : "))
            examgrade["Midterm"] = midtermgrade
            examgrade["Final"] = finalgrade
            examgrade["Project"] = projectgrade
            
            passingaverage = ((midtermgrade*30)/100) + ((finalgrade*50)/100) + ((projectgrade*20)/100)
            if passingaverage>90:
                print(f"{examlesson} your grade is AA. Congratulations")
                break
            elif 70<passingaverage<90:
                print(f"{examlesson} your grade is BB. Congratulations")
                break
            elif 50<passingaverage<70:
                print(f"{examlesson} your grade is CC. Congratulations")
                break
            elif 30<passingaverage<50:
                print(f"{examlesson} your grade is DD.")
                break
            else:
                print(f"{examlesson} your grade is FF. You stayed in class.")
                break

        else:
            print("If your course number is less than 3, it cannot be more than 5.")
            break

    
    elif (name != enteredname or surname != enteredsurname) and enterednumber != 0:
        enterednumber -= 1
        if enterednumber>0:
            print("You wrote wrong, please try again.")
            again=input(f"{name} {surname} do you want to login again? (y/n): ")
            if again == "y":
                continue
            else:
                break
        else:
            print("Please try again later")
            break 
