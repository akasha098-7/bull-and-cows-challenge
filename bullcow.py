import random

def generate_number():
    digits = random.sample('123456789', 4)  # pick 4 unique digits from 1–9
    return ''.join(digits)

def is_valid_guess(guess):
    return (
        guess.isdigit()
        and len(guess) == 4
        and all('1' <= d <= '9' for d in guess)
        and len(set(guess)) == 4
    )

def bulls_and_cows(secret, guess):
    bulls = sum(s == g for s, g in zip(secret, guess))
    cows = sum(g in secret for g in guess) - bulls
    return bulls, cows

def play_game():
    secret = generate_number()

    while True:
        guess = input("Enter your 4-digit guess (digits 1-9, no repeats): ").strip()
        
        if not is_valid_guess(guess):
            print("Invalid guess! Make sure it's 4 unique digits from 1–9.")
            continue
        
        bulls, cows = bulls_and_cows(secret, guess)
        
        if bulls == 4:
            print(f"🎉 Congratulations! You guessed the number {secret}!")
            break
        else:
            print(f"{bulls} Bulls, {cows} Cows")

if __name__ == "__main__":
    play_game()
