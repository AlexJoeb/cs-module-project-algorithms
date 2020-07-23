import timeit

'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k, cache={}):
    # Initalize `arr`. `arr` will hold the list of maximum found numbers in each window and will be returned at the end of the function.
    arr = []
    
    # Initalizing a cache in the parameters to remember sequences, improving on runtime complexity.
    # Cache Structure = {
    #     "1,3,-5": "3"
    # }

    # Sampe `nums` array: [1, 3, -1, -3, 5, 3, 6, 7]
    for index, num in enumerate(nums):
        # This conditional makes sure there is enough space left in the array to consider the 'windowed' array. 
        # If the window requires 3 integers to be valid and only 2 integers are left in `arr`, the loop breaks.
        if index >= len(nums) - k + 1:
            break
        
        # Create a new instance of an array, splice from current index and increment 'k' indexs
        # to create the 'window'
        check = nums[index:index + k]
        # Parse to string.
        checkToStr = ','.join([str(a) for a in check])

        # Check to see if sequence is in cache.
        if checkToStr in cache:
            # If it is already cached, simply returned cached value. 
            arr.append(cache[checkToStr])
            # Continue to next window.
            continue
        
        # Initalize value that will hold the found max value in window.
        maxnum = None

        # Loop through values in `check`
        for item in check:
            # If maxnum is not assigned or maxnum is less than current item:
            if maxnum == None or item > maxnum:
                # Assign maxnum to `item` (the new highest number found)
                maxnum = item
            # Else if `maxnum` is assigned and/or `item` is less than `maxnum`
            else: continue
            
        # Append `maxnum` to the `arr`.
        arr.append(maxnum)

    # Finally, return `arr` that contains the maximum numbers.
    return arr

if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
