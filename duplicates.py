# Declare variables
mylist = [2,1,3,5,8,7,4,0]   # Our inputs to the program
has_duplicates = False # initialize as false (why?)

# Sort 'myList' (Why do we sort first?)
mylist.sort()

# Loop through 'mylist' with a for-Loop
for index in range(len(mylist)-1):
        # Check if adjacent elements of 'mylist' are the same
    print(mylist[index], mylist[index+1])
        # if they are the same, set has_duplicates to True
    if (mylist[index]) == (mylist[index+1]):
        has_duplicates = True
        break
                # Exit out of the for-loop (no need to check rest of list)
print(has_duplicates) # Our outputs of the program
