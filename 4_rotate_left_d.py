def rotate_left_1(arr, d):
    n = len(arr)
    for i in range(d):
        temp = arr[0]
        for j in range(n-1):
            arr[j] = arr[j+1]
        arr[n-1] = temp
    return arr

# juggling algorithm
import math
def rotate_left_2(arr, d):
    n = len(arr)
    d = d % n
    cycles = math.gcd(n, d)
    for i in range(cycles):
        start_ele = arr[i]
        currIdx = i
        while True:
            nextIdx = (currIdx + d) % n
            if nextIdx == i:
                break
            arr[currIdx] = arr[nextIdx]
            currIdx = nextIdx
        arr[currIdx] = start_ele
    return arr

# reversing algorithm
def rotate_left_3(arr, d):
    n = len(arr)
    reverse(arr, 0, d-1)
    reverse(arr, d, n-1)
    reverse(arr, 0, n-1)
    return arr

# helper for rotate_left_3 function
def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1


if __name__ == '__main__':
    tcs = []
    tcs.append([[1,2,3,4,5,6], 2])
    tcs.append([[1,2,3,4,5,6,7], 5])
    for i, tc in enumerate(tcs):
        arr = tc[0]
        d = tc[1]
        # ans = rotate_left_1(arr, d)
        ans = rotate_left_2(arr, d)
        # ans = rotate_left_3(arr, d)
        print(f"tc:{i+1}, ans:{ans}, d:{d}")
