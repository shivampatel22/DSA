def lcm(a, b):
    if a == b:
        return a
    else:
        return int((a*b)/gcd(a, b))
        
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)
        
if __name__ == '__main__':
    a, b = map(int,input().split())
    print(lcm(a, b))
        