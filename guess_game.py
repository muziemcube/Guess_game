guess = 'wrong'
guess_num = random.randint(1, 10)
guess_count = 0

while guess != guess_num:
    guess_count += 1

    guess = int(input("Please guess number between 1-10"))

    if guess == guess_num:
        print("Congratulation! You guess right")
        break
    else:
        print("You guess wrong. Try again")
print(f"The number of round you went is: {guess_count}")