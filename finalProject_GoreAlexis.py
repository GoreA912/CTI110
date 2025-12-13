#Alexis Gore
#12/12/25
#Final Project
#Trivia Game


hero = {
    "name": ...,
    "score": ...,
    "lives": ...,
    "energy": ...,
    "hints": ...,
    "streak": ...,
    "badges": [...],
    "questions_answered": ...,
    "start_time": ...,
}



import random
import time

# ----------------------------
# Question Bank (multiple-choice)
# Each question has: prompt, options, correct_index
# ----------------------------
QUESTION_BANK = [
    {
        "prompt": "What is the capital of France?",
        "options": ["Berlin", "Madrid", "Paris", "Rome"],
        "correct_index": 2,
        "category": "Geography",
        "difficulty": "Easy",
    },
    {
        "prompt": "Which planet is known as the Red Planet?",
        "options": ["Venus", "Mars", "Jupiter", "Saturn"],
        "correct_index": 1,
        "category": "Science",
        "difficulty": "Easy",
    },
    {
        "prompt": "Who wrote 'To Kill a Mockingbird'?",
        "options": ["Harper Lee", "Mark Twain", "George Orwell", "F. Scott Fitzgerald"],
        "correct_index": 0,
        "category": "Literature",
        "difficulty": "Medium",
    },
    {
        "prompt": "What is the smallest prime number?",
        "options": ["0", "1", "2", "3"],
        "correct_index": 2,
        "category": "Math",
        "difficulty": "Easy",
    },
    {
        "prompt": "Which element has the chemical symbol 'O'?",
        "options": ["Gold", "Oxygen", "Osmium", "Silver"],
        "correct_index": 1,
        "category": "Science",
        "difficulty": "Easy",
    },
    {
        "prompt": "In computing, what does 'CPU' stand for?",
        "options": ["Central Processing Unit", "Computer Power Unit", "Core Performance Utility", "Central Program Unit"],
        "correct_index": 0,
        "category": "Tech",
        "difficulty": "Easy",
    },
    {
        "prompt": "Which ocean is the largest?",
        "options": ["Atlantic", "Indian", "Arctic", "Pacific"],
        "correct_index": 3,
        "category": "Geography",
        "difficulty": "Medium",
    },
    {
        "prompt": "What year did the World Wide Web become publicly available?",
        "options": ["1989", "1991", "1995", "2000"],
        "correct_index": 1,
        "category": "Tech",
        "difficulty": "Medium",
    },
    {
        "prompt": "Which artist painted the Mona Lisa?",
        "options": ["Vincent van Gogh", "Leonardo da Vinci", "Pablo Picasso", "Claude Monet"],
        "correct_index": 1,
        "category": "Art",
        "difficulty": "Easy",
    },
    {
        "prompt": "What is the chemical formula for table salt?",
        "options": ["NaCl", "H2O", "CO2", "KCl"],
        "correct_index": 0,
        "category": "Science",
        "difficulty": "Medium",
    },
]

# ----------------------------
# Utility functions
# ----------------------------
def build_hero(name: str) -> dict:
    """Create the main character represented by a dictionary."""
    return {
        "name": name,
        "score": 0,
        "lives": 3,
        "energy": 100,            # 0–100; low energy can cost a life
        "hints": 1,               # start with one hint token
        "streak": 0,              # consecutive correct answers
        "badges": [],             # list of badge names earned
        "questions_answered": 0,  # counter
        "start_time": time.perf_counter(),
    }

def print_status(hero: dict):
    """Display current player status."""
    print("\n--- Status ---")
    print(f"Player: {hero['name']} | Score: {hero['score']} | Lives: {hero['lives']} "
          f"| Energy: {hero['energy']} | Hints: {hero['hints']} | Streak: {hero['streak']}")
    if hero["badges"]:
        print(f"Badges: {', '.join(hero['badges'])}")
    else:
        print("Badges: (none)")
    print("----------------\n")

def award_badges(hero: dict):
    """Grant badges based on score and streak milestones."""
    if hero["score"] >= 50 and "Rising Star" not in hero["badges"]:
        hero["badges"].append("Rising Star")
        print("🏅 Badge earned: Rising Star (50+ points)")
    if hero["streak"] >= 3 and "On a Roll" not in hero["badges"]:
        hero["badges"].append("On a Roll")
        print("🏅 Badge earned: On a Roll (3+ correct in a row)")
    if hero["score"] >= 100 and "Trivia Ace" not in hero["badges"]:
        hero["badges"].append("Trivia Ace")
        print("🏅 Badge earned: Trivia Ace (100+ points)")

def maybe_random_event(hero: dict):
    """Occasional random event that modifies hero's attributes."""
    roll = random.random()  # 0.0 to 1.0
    if roll < 0.15:
        print("🎲 Random event: You found a power snack! Energy +15.")
        hero["energy"] = min(100, hero["energy"] + 15)
        time.sleep(0.8)
    elif roll < 0.30:
        print("🎲 Random event: You tripped rushing to the next question. Energy -10.")
        hero["energy"] = max(0, hero["energy"] - 10)
        time.sleep(0.8)
    elif roll < 0.40:
        print("🎲 Random event: Bonus hint token!")
        hero["hints"] += 1
        time.sleep(0.6)
    # Energy penalty may cost a life if it hits zero
    if hero["energy"] == 0:
        print("⚠️ Energy depleted! You lose a life and recover some energy.")
        hero["lives"] -= 1
        hero["energy"] = 50
        time.sleep(0.8)

def use_hint(question: dict, hero: dict) -> list:
    """
    Use a hint to eliminate two wrong options if available.
    Returns a filtered options list preserving the correct choice.
    """
    if hero["hints"] <= 0:
        print("❌ No hints left.")
        return question["options"]

    hero["hints"] -= 1
    correct_idx = question["correct_index"]
    wrong_indices = [i for i in range(len(question["options"])) if i != correct_idx]
    # Randomly keep one wrong option and the correct one (50/50 style)
    keep_wrong = random.choice(wrong_indices)
    filtered = []
    for i, opt in enumerate(question["options"]):
        if i == correct_idx or i == keep_wrong:
            filtered.append(opt)

    print("💡 Hint used! Two options remain (one correct, one incorrect).")
    return filtered

def ask_question(hero: dict, question: dict) -> bool:
    """Ask a single multiple-choice question; update hero based on outcome."""
    prompt = question["prompt"]
    options = question["options"][:]
    correct_idx = question["correct_index"]

    # Shuffle options but remember where the correct one goes
    paired = list(enumerate(options))  # [(original_index, option), ...]
    random.shuffle(paired)
    shuffled_options = [opt for _, opt in paired]
    new_correct_idx = next(i for i, (orig, _) in enumerate(paired) if orig == correct_idx)

    print(f"\n📚 {question['category']} ({question['difficulty']})")
    print(prompt)

    # Offer hint choice
    filtered_options = shuffled_options
    use_hint_choice = None
    if hero["hints"] > 0:
        use_hint_choice = input("Type 'hint' to use a hint, or press Enter to continue: ").strip().lower()
    if use_hint_choice == "hint":
        # We need to re-map filtered options to the shuffled set
        # Find the correct option text first
        correct_text = shuffled_options[new_correct_idx]
        # Build a pseudo-question to reuse use_hint
        pseudo_q = {
            "options": shuffled_options,
            "correct_index": new_correct_idx
        }
        filtered_options = use_hint(pseudo_q, hero)

    # Show options
    print("\nChoose the correct answer:")
    labeled = []
    for i, opt in enumerate(filtered_options):
        label = chr(ord('A') + i)
        labeled.append((label, opt))
        print(f"  {label}) {opt}")

    # Start timer for speed bonus
    t0 = time.perf_counter()
    answer = input("\nYour choice (A/B/C/D...): ").strip().upper()
    t1 = time.perf_counter()
    elapsed = t1 - t0

    # Map answer letter to index
    try:
        ans_idx = ord(answer) - ord('A')
        if not (0 <= ans_idx < len(filtered_options)):
            raise ValueError
    except Exception:
        print("Invalid input. Counting as incorrect.")
        ans_idx = -1

    # Determine correctness by comparing selected option text to correct option text
    correct_text = shuffled_options[new_correct_idx]
    selected_text = filtered_options[ans_idx] if 0 <= ans_idx < len(filtered_options) else None
    is_correct = (selected_text == correct_text)

    # Update hero dictionary based on outcome
    hero["questions_answered"] += 1

    base_points = 10
    speed_bonus = 0
    if is_correct:
        # Speed bonus: faster than 4 seconds -> +5, faster than 2 seconds -> +10
        if elapsed <= 2.0:
            speed_bonus = 10
        elif elapsed <= 4.0:
            speed_bonus = 5

        earned = base_points + speed_bonus
        hero["score"] += earned
        hero["streak"] += 1
        hero["energy"] = min(100, hero["energy"] + 5)  # a bit of energy for a correct answer

        print(f"✅ Correct! +{base_points} points", end="")
        if speed_bonus:
            print(f" and +{speed_bonus} speed bonus", end="")
        print(f". (Answered in {elapsed:.2f}s)")
    else:
        hero["lives"] -= 1
        hero["streak"] = 0
        hero["energy"] = max(0, hero["energy"] - 10)

        print(f"❌ Incorrect. The correct answer was: {correct_text}. (You took {elapsed:.2f}s)")
        print("You lost a life and some energy.")

    award_badges(hero)
    maybe_random_event(hero)
    print_status(hero)
    return is_correct

def end_summary(hero: dict):
    """Print final summary and grade."""
    total_time = time.perf_counter() - hero["start_time"]
    print("\n====================")
    print("      Game Over     ")
    print("====================")
    print(f"Player: {hero['name']}")
    print(f"Score: {hero['score']}")
    print(f"Lives left: {hero['lives']}")
    print(f"Questions answered: {hero['questions_answered']}")
    print(f"Total time: {total_time:.1f}s")
    if hero["badges"]:
        print(f"Badges: {', '.join(hero['badges'])}")
    else:
        print("Badges: (none)")

    # Simple grading
    if hero["score"] >= 100:
        grade = "A"
    elif hero["score"] >= 70:
        grade = "B"
    elif hero["score"] >= 40:
        grade = "C"
    else:
        grade = "D"
    print(f"Grade: {grade}")

def main():
    print("==============================================")
    print("       Welcome to the Python Trivia Quest     ")
    print("==============================================")
    name = input("Enter your hero's name: ").strip() or "Player"
    hero = build_hero(name)
    print_status(hero)

    questions = QUESTION_BANK[:]
    random.shuffle(questions)

    # Play until out of lives or questions are exhausted
    for q in questions:
        if hero["lives"] <= 0:
            print("You've run out of lives!")
            break
        correct = ask_question(hero, q)
        time.sleep(0.5)  # small pacing delay

    end_summary(hero)

if __name__ == "__main__":
    main()


