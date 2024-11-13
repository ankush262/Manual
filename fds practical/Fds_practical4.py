'''write a python program to store first year percentage in
 array write function for sorting array of floating number in
ascending order using
a) selectin sort 
b) bubble sort and display top five scores'''

#  a) selection sort algoritm
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


# b) bubble sort and display top five scores
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr[:5]





num_students = int(input("Enter the number of students: "))
percentages = []
for i in range(num_students):
    while True:
        try:
            percentage = float(input(f"Enter percentage for student {i + 1}: "))
            if 0 <= percentage <= 100:
                percentages.append(percentage)
                break
              # Exit the loop if the input is valid
            else:
                 print("Please enter a percentage between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

   
sort = selection_sort(percentages)
print("selection sort : ",sort)
sorte = bubble_sort(percentages)
print("bubble sort : ", sorte)
  