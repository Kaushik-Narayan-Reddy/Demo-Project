# Importing the library random in python
import random as rand

# Function to create an array consisting of 25 random integers
def arr_ran():
    
    # Intialising an array
    arr=[]
    
    # Limits of the range for the random values
    x=int(input("Enter starting value for range of numbers: "))
    y=int(input("Enter ending value for range of numbers: "))
    
    # Loop to append 25 random integers to the array within given range
    for i in range(0,25):
        arr.append(rand.randint(x, y))
    
    # Returns a new array with 25 random variables
    return arr

# Function to linearly search through an array to search for a particular
# user defined value
def arr_lin(arr):
    
    # The input value taken from the user
    x=int(input("Enter number to be searched: "))
    
    # Variable used to determine if value is present in array
    a=0
    
    for i in range(len(arr)):
        
        # Compares with each value of the array to search for the user 
        # defined value
        if(arr[i]==x):
            print("Number exists at position "+str(i)+"\n")
            
        # If the integer in the array and given integer do not match
        # variable "a" is appended by 1
        else: 
            a=a+1
            
    # If no array value matches with given value, then value does not 
    # exist hence value of a will be 25 
    if(a==25):
        print("Number does not exist! \n")
        
# F
def arr_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    print(arr)

arr=arr_ran()
print(arr)
arr_lin(arr)
arr_sort(arr)