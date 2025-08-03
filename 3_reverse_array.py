def reverse_1(arr):
    temp = []
    n = len(arr)
    for i in range(n-1, -1, -1):
        temp.append(arr[i])
    return temp

def reverse_2(arr):
    n = len(arr)
    left, right = 0, n-1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr

def reverse_3(arr):
    n = len(arr)
    for i in range(n//2):
        arr[i], arr[n-i-1] = arr[n-i-1], arr[i]
    return arr


if __name__ == '__main__':
    tcs = []
    tcs.append([1,2,3,4,5,6])
    for i, arr in enumerate(tcs):
        # ans = reverse_1(arr)
        # ans = reverse_2(arr)
        ans = reverse_3(arr)
        print(f"tc:{i+1}, ans:{ans}")