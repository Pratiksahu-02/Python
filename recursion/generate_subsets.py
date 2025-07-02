def generate_substrings(arr, current=[], index=0):
    arr.sort()
    if index == len(arr):
        print(sorted(current))
        return
    generate_substrings(arr, current, index+1)
    generate_substrings(arr, current+[arr[index]], index+1)
    return


a=generate_substrings([1,2,3])