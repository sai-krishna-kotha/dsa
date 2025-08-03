def stock_buy_sell_1(price, start, end):
    res = 0
    # i stands for the day you buy a stock
    for i in range(start, end):
        # j stands for the day you sell a stock
        for j in range(i+1, end+1):
            if price[j] > price[i]:
                curr = (price[j] - price[i]) + \
                stock_buy_sell_1(price, start, i-1) + \
                stock_buy_sell_1(price, j+1, end)
                res = max(res, curr)
    return res

def stock_buy_sell_2(price):
    l_mini = price[0]
    l_maxi = price[0]
    n = len(price)
    i = 0
    ans = 0
    while i < n - 1:
        while i < n - 1 and price[i] >= price[i+1]:
            i += 1
        l_mini = price[i]
        while i < n -1 and price[i] <=price[i+1]:
            i += 1
        l_maxi = price[i]
        ans += l_maxi - l_mini
    return ans

def stock_buy_sell_3(price):
    n = len(arr)
    ans = 0
    for i in range(n-1):
        if arr[i] < arr[i+1]:
            ans += (arr[i+1] - arr[i])
    return ans


if __name__ == '__main__':
    tcs = []
    tcs.append([100, 180, 260, 310, 40, 535, 695])
    for i, arr in enumerate(tcs):
        # ans = stock_buy_sell_1(arr, 0, len(arr))
        # ans = stock_buy_sell_2(arr)
        ans = stock_buy_sell_3(arr)
        print(f"tc:{i+1}, ans:{ans}")