def majority_ele_1(arr):
    n = len(arr)
    ans = []
    for i in range(n):
        cnt = 1
        for j in range(i+1, n):
            if arr[i] == arr[j]:
                cnt += 1
        if cnt > n//3:
            ans.append(arr[i])
    if len(ans) == 2:
        if ans[0] < ans[1]:
            return ans
        ans[0], ans[1] = ans[1], ans[0]
        return ans
    return ans

def majority_ele_2(arr):
    n = len(arr)
    freq = {}
    ans = []
    for i in arr:
        freq[i] = freq.get(i, 0) + 1
    for k, v in freq.items():
        if v > n // 3:
            ans.append(k)
    if len(ans) == 2 and ans[0] > ans[1]:
        ans[0], ans[1] = ans[1], ans[0]
    return ans

def moore_voting_algo(arr):
    n = len(arr)
    cand = -1
    cnt = 0
    for ele in arr:
        if cnt == 0:
            cand = ele
            cnt = 1
        elif cand == ele:
            cnt += 1
        else:
            cnt -= 1
    if arr.count(cand) > n//2:
        return cand
    return -1

if __name__ == '__main__':
    tcs = []
    # tcs.append([2,2,1,1,1,2,3])
    tcs.append([2,1,1,1,1,3,5,1,1,2])
    for i, arr in enumerate(tcs):
        # ans = majority_ele_1(arr)
        ans = majority_ele_2(arr)
        # moore_ans = moore_voting_algo(arr)
        # print(f"Moore's voting algo got :{moore_ans}")
        print(f"tc:{i+1}, ans:{ans}")