# https://www.codechef.com/submit/HOTCOLD
# cook your dish here
# read the number of test cases
T = int(input())
for tc in range(T):
    print('HOT' if int(input()) > 20 else 'COLD')
