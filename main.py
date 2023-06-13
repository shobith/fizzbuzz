def fizzbuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return "fizz buzz"
    elif n % 3 == 0:
        return "fizz"
    elif n % 5 == 0:
        return "buzz"
    else:
        return str(n)

def main():
    for n in range(1, 101):
        print(fizzbuzz(n))

if __name__ == '__main__':
    main()