# Task 1
def hello():
  return "Hello!"

# Task 2
def greet(name):
  return "Hello, " + name.capitalize() + "!"

# Task 3
def calc(num1, num2, operator = "multiply"):
  try:
    match operator:
      case "add":
        return num1 + num2
      case "subtract":
        return num1 - num2
      case "multiply":
        return num1 * num2
      case "divide":
        return num1 / num2
      case "modulo":
        return num1 % num2
      case "int_divide":
        return num1 // num2
      case _:
        print("Operator not found in my list!")
  except ZeroDivisionError:
    return "You can't divide by 0!"
  except TypeError:
    return f"You can't {operator} those values!"
  else:
    return "An unexpected error occured!"

# Task 4
def data_type_conversion(value, to_data_type):
  try:
    match to_data_type:
      case "float":
        return float(value)
      case "str":
        return str(value)
      case "int":
        return int(value)
      case _:
        return "Data type not supported."
  except:
    return f"You can't convert {value} into a {to_data_type}."

# Task 5
def grade(*grades):
  try:
    average = sum(grades) // len(grades)
  except:
    return "Invalid data was provided."

  if average < 60:
    return "F"
  elif average < 70:
    return "D"
  elif average < 80:
    return "C"
  elif average < 90:
    return "B"
  else:
    return "A"

# Task 6:
def repeat(string, count):
  new_str = ""

  for i in range(count):
    new_str += string

  return new_str

# Task 7:
def student_scores(param, **score_list):
  if param == "best":
    sorted_list = sorted(score_list.items())
    sorted_dict = dict(sorted_list)
    return list(sorted_dict.keys())[0]
  elif param == "mean":
    return sum(score_list.values())/len(score_list.values())

# Task 8
def titleize(string):
  words = string.split()

  little_word_list = ["a", "on", "an", "the", "of", "and", "is", "in"]

  def cap_big_word(word):
    if word in little_word_list:
      return word
    else:
      return word.capitalize()

  capitalized_words = list(map(cap_big_word, words))
  capitalized_words[0] = words[0].capitalize()
  capitalized_words[-1] = words[-1].capitalize()

  return " ".join(capitalized_words)

# Task 9
def hangman(secret, guess):
  guess_letters = list(guess)
  secret_letters = list(secret)
  response_letters = []

  for i in range(len(secret_letters)):
    if secret_letters[i] in guess_letters:
      response_letters.append(secret_letters[i])
    else:
      response_letters.append("_")

  return "".join(response_letters)

# Task 10
def pig_latin(string):
  words = string.split()

  def convert_to_pig_latin(word):
    vowels = ("a", "e", "i", "o", "u")

    if word.startswith(vowels):
      return word + "ay"
    else:
      break_index = 0
      for i in range(len(word)):
        if word[i] == "q":
          break_index = i + 2
        elif word[i] not in vowels:
          break_index = i + 1
        else:
          break
      return word[break_index:] + word[:break_index] + "ay"

  pig_latin_words = list(map(convert_to_pig_latin, words))
  return " ".join(pig_latin_words)
