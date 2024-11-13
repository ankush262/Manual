'''Write a Python program to store second year percentage of students in array. Write function 
for sorting array of floating point numbers in ascending order using  
a) Insertion sort  
b) Shell Sort and display top five scores '''

def main():
    # Initialize an empty list to store second-year percentages of students
    second_year_percentage = []
    while True:
        try:
            no_of_students = int(input("Enter the number of students in second year: "))
            break
        except ValueError:
            print("Invalid input. Please enter a number.")
            
    for i in range(no_of_students):
        try:
            percentage = float(input(f"Enter the second-year percentage of student {i+1}: "))
            if 0 <= percentage <= 100:
                second_year_percentage.append(percentage)
                
            else:
                print("Percentage must be between 0 and 100. Try again.")
                break
        except ValueError:
                print("Invalid input. Please enter a valid number.")
        
    
    print("Second year percentages of students:", second_year_percentage)

    # Sorting using Insertion Sort
    insertion_sort(second_year_percentage)
    print("Sorted array using Insertion Sort:", second_year_percentage)
    print("Top five scores using Insertion Sort:", display_top_five(second_year_percentage))

    # Sorting using Shell Sort
    shell_sorted_percentage = second_year_percentage.copy()
    shell_sort(shell_sorted_percentage)
    print("Sorted array using Shell Sort:", shell_sorted_percentage)
    print("Top five scores using Shell Sort:", display_top_five(shell_sorted_percentage))


def display_top_five(arr):
    """Returns the top five scores from the sorted array."""
    top_five = arr[-5:]  
    return top_five


# a) Insertion sort
def insertion_sort(arr):
    """Sorts an array of floating point numbers using Insertion Sort."""
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
       
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


# b) Shell sort
def shell_sort(arr):
    """Sorts an array of floating point numbers using Shell Sort."""
    n = len(arr)
    gap = n // 2  
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2  # Reduce the gap size


if __name__ == "__main__":
    main()



    

main()