from project import generate_flashcards, shuffle_flashcards

def test_generate_flashcards():
    """
    Teste que la fonction génère bien une liste de flashcards avec des questions et réponses.
    """
    cards = generate_flashcards("Python")
    assert isinstance(cards, list)                          # Vérifie que le résultat est bien une liste
    assert len(cards) >= 2                                  # Vérifie qu'il y a au moins 2 cartes
    assert "question" in cards[0] and "answer" in cards[0]  # Vérifie les clés dans le dictionnaire

def test_shuffle_flashcards():
    """
    Teste que le mélange des cartes ne change pas leur contenu.
    """
    cards = generate_flashcards("Python")
    shuffled = shuffle_flashcards(cards.copy())  # Copie pour ne pas altérer la version originale
    # Vérifie que les questions sont identiques (contenu non modifié)
    assert set(card["question"] for card in cards) == set(card["question"] for card in shuffled)

def test_shuffle_preserves_length():
    """
    Teste que le nombre de cartes reste le même après le mélange.
    """
    cards = generate_flashcards("Math")
    assert len(shuffle_flashcards(cards)) == len(cards)