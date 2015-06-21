def fizz_buzz(i):
        if i == 0:
            return 0
        elif i % 15 == 0:
            return 'FizzBuzz'
        elif i % 3 == 0:
            return 'Fizz'
        elif i % 5 == 0:
            return 'Buzz'
        else:
            return i

