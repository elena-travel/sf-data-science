import numpy as np

def score_game(random_predict) -> int:
    """За какое количество попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попытки")


def game_core_v3(number: int = 1) -> int:
    """Функция, которая угадывает число за минимальное число ходов
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    # Ваш код начинается здесь
    count = 0
    min_num = 1
    max_num = 100
    predict = (max_num - (min_num-1))//2
    
    while number != predict:
        count += 1
        if number > predict:
            min_num = predict + 1
            predict = (max_num + min_num + 1)//2
        elif number < predict:
            max_num = predict - 1
            predict = (max_num - (min_num-1))//2
    return count
    # Ваш код заканчивается здесь

print('Run benchmarking for game_core_v3: ', end='')
score_game(game_core_v3)