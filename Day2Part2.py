# Opponent is going to play in first column
# A is for Rock
# B is for Paper
# C is for Scissors

# Second column is what you should play
# X for Rock
# Y for Paper
# Z for Scissors

# Score based on what you picked
# 1 for Rock
# 2 for Paper
# 3 for Scissors

# Score also based on result
# 0 for loss
# 3 for draw
# 6 for win

with open('Day2.txt') as f:
    score = 0
    while True:
        line = f.readline()
        if not line:
            print(score)
            break
        them = line[0]
        me = line[2]
        if me == 'X':
            score += 0
            if them == 'A':
                score += 3
            elif them == 'B':
                score += 1
            elif them == 'C':
                score += 2
        elif me == 'Y':
            score += 3
            if them == 'A':
                score += 1
            elif them == 'B':
                score += 2
            elif them == 'C':
                score += 3
        elif me == 'Z':
            score += 6
            if them == 'A':
                score += 2
            elif them == 'B':
                score += 3
            elif them == 'C':
                score += 1