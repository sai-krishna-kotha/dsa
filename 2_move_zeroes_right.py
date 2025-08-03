def move_zeroes_1(arr):
    n = len(arr)
    temp = [0] * n
    k = 0
    for i in range(n):
        if arr[i] != 0:
            temp[k] = arr[i]
            k += 1
    return temp
def move_zeroes_2(arr):
    n = len(arr)
    cnt = 0
    for i in range(n):
        if arr[i] != 0:
            arr[cnt] = arr[i]
            cnt += 1
    for i in range(cnt, n):
        arr[i] = 0
    return arr

def move_zeroes_3(arr):
    n = len(arr)
    cnt = 0
    for i in range(n):
        if arr[i] != 0:
            temp = arr[i]
            arr[i] = arr[cnt]
            arr[cnt] = temp 
            cnt += 1
    return arr
if __name__ == '__main__':
    tcs = []
    tcs.append([1,2,0,4,3,0,0,5,0])
    tcs.append([10,20,30])
    tcs.append([0,0])
    for i, arr in enumerate(tcs):
        # ans = move_zeroes_1(arr)
        # ans = move_zeroes_2(arr)
        ans = move_zeroes_3(arr)
        print(f"tc:{i+1}, ans:{ans}, arr:{arr}")