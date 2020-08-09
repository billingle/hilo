from random import randint


def main():
    print("Welcome to the game of High-Low.")

    name = input("what is your name: ")
    secret_num = randint(1, 100)
    print("I have a secret number from 1 to 100.")

    while True:
        guess = int(input("Guess the secret number : "))
        if guess > secret_num:
            print("Sorry {}, {} is higher than the secret number.".format(name, guess))
        elif guess < secret_num:
            print("Sorry {}, {} is lower than the secret number.".format(name, guess))
        else:
            break

    print("You guessed the secret number {}, it is {}".format(name, secret_num))
    exit()


if __name__ == '__main__':
    main()
