from random import randint
def dice_simulator(n: int) -> list[int]:
    if n < 1:
        raise ValueError
    rolls: list[int] = []

    for i in range(n):
        rolls.append(randint(1, 6))
    return rolls

def main():
    print("Enter exit to quit!")
    while True:
        try:
            user_input: str = input("How many times you want to roll a dice? ")
            if user_input.lower() == 'exit':
                print("Thanks for playing!")
                break
            print(*dice_simulator(int(user_input)), sep=", ")

        except ValueError:
            print("An integer must be entered.")

if __name__ == "__main__":
    main()