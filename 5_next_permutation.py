def next_permutation(arr):
    n = len(arr)
    pivot = -1
    for i in range(n-1, 0, -1):
        if arr[i] > arr[i-1]:
            pivot = i-1
            break
    if pivot == -1:
        arr.reverse()
        return arr
    for i in range(n-1, pivot, -1):
        if arr[pivot] < arr[i]:
            arr[pivot], arr[i] = arr[i], arr[pivot]
            break
    left = pivot+1
    right = n-1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr

if __name__ == '__main__':
    tcs = []
    tcs.append([1,2,3,7,45,1])
    tcs.append([5,2,4,3,1])
    for i, arr in enumerate(tcs):
        ans = next_permutation(arr)
        print(f"tc:{i+1}, ans:{arr}")
        