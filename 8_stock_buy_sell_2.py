def stock_buy_sell_1(price):
    n = len(price)
    ans = 0
    for i in range(n-1):
        for j in range(i+1, n-1):
            if price[j] > price[i]:
                ans = max(ans, price[j]-price[i])
    return ans

def stock_buy_sell_2(price):
    n = len(price)
    mini = price[0]
    ans = 0
    for ele in price:
        mini = min(mini, ele)
        ans = max(ans, ele-mini)
    return ans

if __name__ == '__main__':
    tcs = []
    tcs.append([7,10,1,3,6,9,2])
    for i, arr in enumerate(tcs):
        # ans = stock_buy_sell_1(arr)
        ans = stock_buy_sell_2(arr)
        print(f"tc:{i+1}, ans:{ans}")
