import random
def main():
    """
    Fonction principale qio acceuille le user, lui demande un sujet, génère des flashcards et lance le quiz
    """
    print("Welcome to the Flashcard Quiz!")
    text = input("Please enter a topic for your flashcards: ")
    flashcards = generate_flashcards(text)
    flashcards = shuffle_flashcards(flashcards) 
    run_quiz(flashcards) 

def generate_flashcards(topic):
    """
    Fonction qui génère des flashcards à partir d'un sujet donné
    """
    return [
        {"question": f"What is {topic}?", "answer": f"{topic} is a concept to study."},
        {"question": f"Why is {topic} important?", "answer": f"It helps understand {topic} better."}
    ]

def shuffle_flashcards(flashcards):
    """
    Fonction qui mélange les flashcards
    """
    random.shuffle(flashcards)
    return flashcards


def run_quiz(flashcards):
    """
    Fonction qui fait défiler chaque flashcard, pose la question à l'utilisateur, puis attend la réponse
    """
    for card in flashcards:
        answer = input(card["question"] + " ")  # ✅ corrigé ici
        if answer.lower() in card["answer"].lower():
            print("Correct!")
        else:
            print(f"Incorrect! The correct answer is: {card['answer']}")


if __name__ == "__main__":
    main()
