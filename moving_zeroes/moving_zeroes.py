'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    for index, item in enumerate(arr):
        if item != 0:
            arr.pop(index)
            arr.insert(0, item)
        else: continue
    return arr

if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")