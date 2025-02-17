import json
import random
import time

LEVEL_FILE = 'level.json'


# read level from level.json
def get_data():
  with open(LEVEL_FILE, 'r', encoding='utf-8') as file:
    data = json.load(file)
    return data


# make level.json to store level if not exist
def check_file():
  try:
    get_data()
  except Exception as e:
    with open(LEVEL_FILE, 'w', encoding='utf-8') as file:
      data = {
          'level': 1,
          'attempt': 0,
      }
      json.dump(data, file, indent=4)


# flip a coin n (level) times
def flip_coin():
  face = ['H', 'T']
  return random.choice(face)


def flip_coins(level):
  results = []
  for i in range(level):
    result = flip_coin()
    results.append(result)
  return results


# increase attempt
def increase_attempt(attempt):
  data = get_data()
  with open(LEVEL_FILE, 'w', encoding='utf-8') as file:
    new_data = {**data, 'attempt': attempt}
    json.dump(new_data, file, indent=8)


# if coin results is all Heads, increase level
def check_win(results):
  for result in results:
    if result == 'T':
      return False
  return True


def increase_level(level):
  level += 1
  data = get_data()
  with open(LEVEL_FILE, 'w', encoding='utf-8') as file:
    new_data = {**data, 'level': level}
    json.dump(new_data, file, indent=8)


# reset level
def reset_level():
  with open(LEVEL_FILE, 'w', encoding='utf-8') as file:
    data = {'level': 1, 'attempt': 0}
    json.dump(data, file, indent=4)


def game():
  check_file()
  print('Press ENTER to flip coins')
  print('Flip all HEADS to win and level up')
  print('Type [reset] to reset your level')
  print('Type [exit] to quit the program')
  print('\n\n\n')

  while True:
    print()
    data = get_data()
    level = data.get('level')
    attempt = data.get('attempt')
    print(f"Level: {level}", flush=True)
    print(f"Winning chance: {(1/2)**level * 100}%")
    action = input('> ')
    print('\033[F\033[K' * 7, end='', flush=True)
    if action == 'exit':
      print('bye.')
      break
    elif action == 'reset':
      print('\nLevel has been reset to 1\n')
      reset_level()
    else:
      attempt += 1
      increase_attempt(attempt)
      print(f"Attempt {attempt}")
      results = flip_coins(level)
      print(f"Results: ", end='', flush=True)
      for i, result in enumerate(results):
        # if i < len(results) - 1:
        #   print(f"{result}, ", end='', flush=True)
        # else:
        #   print(result)
        print(f"{result}, ", end='', flush=True) if i < len(results) - 1 else print(result)
        time.sleep(0.1)
      win = check_win(results)
      if win:
        increase_level(level)
        print('\"nice one!\"', flush=True)
        time.sleep(2)
      else:
        print('\"nt. try again :)\"', flush=True)


if __name__ == '__main__':
  game()
