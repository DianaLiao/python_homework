def make_hangman(secret_word):
  guesses = []

  def hangman_closure(letter):
    guesses.append(letter.lower())

    secret_word_array = list(secret_word.lower())

    displayed_word_array = [char if char in guesses else '_' for char in secret_word_array]

    displayed_word = ''.join(displayed_word_array)
    print(displayed_word)

    if "_" in displayed_word_array:
      return False
    else:
      return True

  return hangman_closure

secret_word = input("Enter a secret word: ")
game = make_hangman(secret_word)
guess = input("Guess a letter: ")

while game(guess) == False:
  guess = input("Guess a letter: ")
  game(guess)
else:
  print("Congratulations! The word was:", secret_word)