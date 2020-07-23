'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    
    # Initalize dictionary to how the amount of times an iteger is seen.
    elems = {}

    # Enumerate through the array of numbers.
    for index, item in enumerate(arr):
        if item not in elems:
            elems[item] = 1
        else:
            elems[item] += 1
        
    # Loop through all the key and value pairs in `elems`. 
    # Find the key that has the value of 1.
    for key, value in elems.items():
        if value == 1:
            return key
        else: continue

    return None


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")