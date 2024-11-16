import random
opponent_history = []
def analyze_sequence(observation, configuration):
    if observation.step == 0:
        return random.randint(0, 2)
    
    global opponent_history
    if observation.step > 0:
        opponent_history.append(int(observation.lastOpponentAction))
    
    if len(opponent_history) < 3:
        return random.randint(0, 2)
    
    # Найдем последнюю последовательность ходов противника
    last_sequence = tuple(opponent_history[-3:])
    
    # Создаем словарь для хранения частот следующих ходов
    next_move_freq = {0: 0, 1: 0, 2: 0}
    
    for i in range(len(opponent_history) - 3):
        current_sequence = tuple(opponent_history[i:i+3])
        if current_sequence == last_sequence:
            next_move = opponent_history[i+3]
            next_move_freq[next_move] += 1
    
    # Выбираем наиболее частый следующий ход
    most_frequent_move = max(next_move_freq, key=next_move_freq.get)
    
    # Возвращаем ход, который победит наиболее частый следующий ход
    return (most_frequent_move + 1) % 3
