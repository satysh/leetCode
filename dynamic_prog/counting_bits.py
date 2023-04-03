'''
Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), 
ans[i] is the number of 1's in the binary representation of i.

Example 1:

Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10

Example 2:

Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101

 

Constraints:

    0 <= n <= 105
'''
def main():
	n = int(input())

	# 6 -> 1 1 0
	# 3 -> 1 1
	# 6 // 2 = 3
	# num of 1's for 6  = num of 1's for 6 // 2 + 6 % 2

	ans = [0] * (n + 1)
	for i in range(1, n + 1):
		ans[i] = ans[i // 2] + i % 2

	print(ans)

if __name__ == '__main__':
	main()