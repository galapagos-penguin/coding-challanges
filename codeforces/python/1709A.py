# http://codeforces.com/problemset/problem/1709/A
# read the number of test cases
T = int(input())
for tc in range(T):
    key = int(input())
    keys = input()
    keys = keys.split(' ')
    for x in range(len(keys)):
        keys[x] = int(keys[x])
    if keys[key-1] == 0:
        print('NO')
        continue
    if keys[keys[key-1]-1] == 0:
        print('NO')
        continue
    print('YES')
