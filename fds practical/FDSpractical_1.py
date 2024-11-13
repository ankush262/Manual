''' In second year computer engineering class, group A student’s play cricket, group B students 
play badminton and group C students play football.  
Write a Python program using functions to compute following: -  
a) List of students who play both cricket and badminton  
b) List of students who play either cricket or badminton but not both  
c) Number of students who play neither cricket nor badminton 
d) Number of students who play cricket and football but not badminton. 
(Note- While realizing the group, duplicate entries should be avoided, Do not use SET built
in functions) '''


# a) List of students who play both cricket and badminton  
def cnb(list1, list2):
    list3 = list(set(list1) & set(list2))
    print("List of students who play both Cricket and Badminton : ", list3)
    return len(list3)
# b) List of students who play either cricket or badminton but not both  
def cob(list1,list2):
    list3 = list(set(list1) ^ set(list2))
    print("List of students who play either Cricket or Badminton but not both : ", list3)
    return len(list3)

# c) Number of students who play neither cricket nor badminton 
def ncb(total_students, list1, list2):
    list3 = list(set(range(1, total_students + 1)) - (set(list1) | set(list2)))
    print("List of students who play neither cricket nor badminton  : ", list3)
    return len(list3)

# d) Number of students who play cricket and football but not badminton. 

def cfb(total_students, list1, list2, list3):
    list4 = list(set(list1) & set(list2) - set(list3))
    print("List of students who play cricket and football but not badminton : ", list4)
    return len(list4)


SE = []
SEtotal = int(input("Enter the total number of student's in SE : "))
for i in range(SEtotal):
    SE.append(input("Enter the name's of student " ))
print("SE : ", SE)

cricket=[]
cricket_numbers = int(input("Enter the total number of student who play cricket : "))
for i in range(cricket_numbers):
    cricket.append(input("Enter the name of the student who play cricket : "))

football =[]
football_numbers = int(input("Enter the total number of student who play football : "))
for i in range(football_numbers):
    football.append(input("Enter the name of the student who play football : "))

badminton = []
badminton_numbers = int(input("Enter the total number of student who play badminton :"))
for i in range(badminton_numbers):
    badminton.append(input("Enter the name of the student who play badminton : "))






while True:
    print("      ------- MENU--------          ")
    print("1) List of students who play both cricket and badminton")
    print("2) List of students who play either cricket or badminton but not both")
    print("3) Number of students who play neither cricket nor badminton")
    print("4) Number of students who play cricket and football but not badminton.")
    print("5) Exit")
    number = int(input("Enter the number: "))
    match number:
        case 1:
            result = cnb(cricket, badminton)
            print(f"Result for case 1: {result}")
            continue_option = input("Do you want to continue? (yes/no): ")
            if continue_option.lower() != "yes":
                break
        
        case 2:
            result = cob(cricket, badminton)
            print(f"Result for case 2: {result}")
            continue_option = input("Do you want to continue? (yes/no): ")
            if continue_option.lower() != "yes":
                break
            
        case 3:
            result = ncb(SEtotal, cricket, badminton)
            print(f"Result for case 3: {result}")
            continue_option = input("Do you want to continue? (yes/no): ")
            if continue_option.lower() != "yes":
                break
            
        case 4:
            result = cfb(SEtotal, cricket, football, badminton)
            print(f"Result for case 4: {result}")
            continue_option = input("Do you want to continue? (yes/no): ")
            if continue_option.lower() != "yes":
                break
            
        case 5:
            continue_option = input("Do you want to continue? (yes/no): ")
            if continue_option.lower() != "yes":
                break
            
        case default:
            continue_option = input("Do you want to continue? (yes/no): ")
            if continue_option.lower() != "yes":
                break


