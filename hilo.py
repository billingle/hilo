from random import randint


def main():
    print("Welcome to the game of High-Low.")

    secret_num = randint(1, 100)
    guess = int(input("Guess the secret number, from 1 to 100 : "))

    while guess != secret_num:
        if guess > secret_num:
            print("Too high.")
        else:
            print("Too low.")
        guess = int(input("Guess the secret number, from 1 to 100 : "))

    print("You guessed the secret number, it is {}".format(secret_num))
    exit()


if __name__ == '__main__':
    main()
