'''Write a Python program to store marks scored in subject “Fundamental of Data Structure” by 
N students in the class. Write functions to compute following: 
a) The average score of class  
b) Highest score and lowest score of class  
c) Count of students who were absent for the test 
d) Display mark with highest frequency '''

import pandas as pd
students  = []
marks = []

total_number_of_students = int(input("Enter the total number of student in class : "))

for i in range(total_number_of_students):
    students.append(input("Enter the name of  the student :  "))
    
print(students)

for i in range(len(students)):
    marks.append(int(input("enter the marks   obtain in fds subject   : ")))

my_dict = {A: B for A, B in zip(students,marks)}

print(my_dict)


# The average score of class 
def average_score(marks):
    sum = 0
    count = 0
    for i in range(len(marks)):
        if marks[i]!=-999:
            sum = sum + marks[i]
            count += 1
    avg = sum/count
    return print(" The average_score is : ", avg)


# Highest score and lowest score of class 

def highest_score(marks):
    sum = 0
    count = 0
    for i in range(len(marks)):
        if marks != -999:
            max = marks[0]
        for i in range(1,len(marks)):
            if marks[i] > max:
                max = marks[i]
    return max


def lowest_score(marks):
    sum = 0
    count = 0
    for i in range(len(marks)):
        if marks != -999:
            min = marks[0]
            for i in range(1,len(marks)):
                if marks[i] < min:
                    min = marks[i]
    return min

#  Count of students who were absent for the test 
def absent(marks):
    count = 0
    for i in range(len(marks)):
        if marks[i] == -999:
            count += 1
    return count


# Display mark with highest frequency
def maxFrequency(marks):
    i=0
    Max=0
    print("Marks  |  Frequency")
    for j in marks:
        if (marks.index(j)==i):
            print(j,"    |  ",marks.count(j))
            if marks.count(j)>Max:
                Max=marks.count(j)
                mark=j
        i=i+1
    return(mark,Max) 

flag = 1
while flag  == 1:
    print("1)  The average score of class ")
    print("2) Highest score and lowest score of class   ")
    print(" 3) Count of students who were absent for the test ")
    print( "  4) Display mark with highest frequency  ")
    print("5) Exit")
    
    number = int(input("enter any number given above : "))
    match number :
        case 1:
            average_score(marks)
            a = input("Do you want to continue (yes/no) :")
            if a == "yes":
                 flag =1
            else:
                 flag = 0
                 print("thanks")  


        case 2:
             print("Highest Score in Class : ", highest_score(marks))
             print("Lowest Score in Class : ", lowest_score(marks))
             a = input("Do you want to continue (yes/no) :")
             if a == "yes":
                 flag =1
             else:
                 flag = 0
                 print("thanks") 

        case 3:
            print("students who were absent : ", absent(marks))
            a = input("Do you want to continue (yes/no) :")
            if a == "yes":
                 flag =1
            else:
                 flag = 0
                 print("thanks")  
        case 4:
            print("marks with max repeatation : ", maxFrequency(marks))
            a = input("Do you want to continue (yes/no) :")
            if a == "yes":
                 flag =1
            else:
                 flag = 0
                 print("thanks")  

                 
        