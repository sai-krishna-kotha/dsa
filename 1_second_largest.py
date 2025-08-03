def second_largest_1(arr):
	arr.sort()
	n = len(arr)
	for i in range(n-1, -1,-1):
		if arr[i] != arr[n-1]:
			return arr[i]
	return -1

def second_largest_2(arr):
	n = len(arr)
	maxi = float('-inf')
	for i in range(n):
		maxi = max(maxi, arr[i])
	ans = float('-inf')
	for i in range(n):
		if arr[i] != maxi:
			ans = max(ans, arr[i])
	return ans if ans != float('-inf') else -1

def second_largest_3(arr):
	n = len(arr)
	maxi = float('-inf')
	ans = float('-inf')
	for i in range(len(arr)):
		if maxi < arr[i]:
			ans = maxi
			maxi = arr[i]
		elif arr[i] != maxi and ans < arr[i]:
			ans = arr[i]
	return ans if ans != float('-inf') else -1
	
	
if __name__ == '__main__':
	tc = []
	tc.append([12,35,1,10,34,35,1])
	tc.append([1,1,1])
	for i, arr in enumerate(tc):
		# ans = second_largest_1(arr)
		# ans = second_largest_2(arr)
		ans = second_largest_3(arr)
		print(f"tc:{i+1}, ans:{ans}, arr:{arr}")
