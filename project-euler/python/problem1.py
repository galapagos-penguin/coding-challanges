# https://projecteuler.net/problem=1
def multiples_of_3_or_5(max):
    s = 0
    for x in range(max):
        if x % 3 == 0 or x % 5 == 0:
            s += x
    return s

if __name__ == '__main__':
    print(multiples_of_3_or_5(1000))
