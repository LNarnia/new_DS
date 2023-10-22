import numpy as np

def game_core_v3(number: int = 1) -> int:
    """
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    # создаем переменную для подсчета количества попыток
    count = 0
    min_num, max_num = 1, 100
    # предполагаемое число
    guess_num = np.random.randint(1, 101)
    
    # цикл для угадывания числа
    # в каждой попытке в два раза уменьшаем количество оставшихся вариантов
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
        game_core_v3 ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    # загадываем список чисел
    random_array = np.random.randint(1, 101, size=(1000)) 

    for number in random_array:
        count_ls.append(game_core_v3(number))
        
    # находим среднее количество попыток
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попытки")
    return score

# RUN
if __name__ == '__main__':
    score_game(game_core_v3)
    