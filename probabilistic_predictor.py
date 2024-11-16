import random

opponent_history = []

def probabilistic_predictor(observation, configuration):
    global opponent_history
    if observation.step == 0:
        return random.randint(0, 2)
    else:
        opponent_history.append(int(observation.lastOpponentAction))
    # Подсчитываем частоту каждого хода противника
    move_counts = [0, 0, 0]
    for move in opponent_history:
        move_counts[move] += 1
    
    # Вычисляем вероятности каждого хода
    total_moves = sum(move_counts)
    probabilities = [count / total_moves for count in move_counts]
    
    # Выбираем ход, который победит наиболее вероятный ход противника
    most_probable_move = probabilities.index(max(probabilities))
    return (most_probable_move + 1) % 3
