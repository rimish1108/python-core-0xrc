import random

print("=" * 50)
print("      TERMINAL HACKER SIMULATOR")
print("=" * 50)

score = 0

while True:
    print("\nChoose a target:")
    print("1. Bank Server")
    print("2. Government Database")
    print("3. Corporate Network")
    print("4. Exit")

    choice = input("> ")

    if choice == "4":
        print(f"\nFinal Score: {score}")
        break

    code = random.randint(1000, 9999)

    print("\nAccess Code Generated!")
    print("Guess the 4-digit code.")

    guess = input("Code: ")

    if guess == str(code):
        print("ACCESS GRANTED")
        score += 100
    else:
        print(f"ACCESS DENIED! Correct code was {code}")
        score -= 25

    print(f"Current Score: {score}")