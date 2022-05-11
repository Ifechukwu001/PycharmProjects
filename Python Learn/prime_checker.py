def prime_checker(number):
    answer = "It is a Prime number"
    for integer in range(2, number):
        if number % integer == 0:
            answer = "It is not a Prime number"
        else:
            print(answer)


n = int(input("Check this number:. "))
prime_checker(number=n)
