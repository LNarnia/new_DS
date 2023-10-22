import numpy as np

def game_core_v3(number: int = 1) -> int:
    """
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    # Ваш код начинается здесь
    count = 0
    min_num, max_num = 1, 100
    guess_num = np.random.randint(1, 101)

    while True:
      count += 1
      if guess_num<number:
        min_num = guess_num + 1
        guess_num = (min_num+max_num) // 2
      elif guess_num>number:
        max_num = guess_num - 1
        guess_num = (min_num+max_num) // 2
      else:
        break

    return count

def score_game(game_core_v3) -> int:
    """За какое количество попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(game_core_v3(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попытки")
    return score

# RUN
if __name__ == '__main__':
    score_game(game_core_v3)
    