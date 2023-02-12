import random

def player(prev_play, opponent_history = []):
    # Randomly choose a move (rock, paper, or scissors)
    move = random.choice(['R', 'P', 'S'])
    
    # Return the move
    return move
