opponent_moves = []
def counter_most_common_agent(observation, configuration):
    global opponent_moves
    if observation.step == 0:
        return 0  # Начинаем с камня
    else:
        opponent_moves.append(int(observation.lastOpponentAction))
    move_counts = [opponent_moves.count(0), opponent_moves.count(1), opponent_moves.count(2)]
    most_common_move = move_counts.index(max(move_counts))
    return (most_common_move + 1) % 3
