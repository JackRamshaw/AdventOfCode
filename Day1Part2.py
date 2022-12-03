with open('Day1.txt') as f:
    max = [0,0,0]
    num = 0
    while True:
        line = f.readline()
        if not line:
            if num > max[0]:
                max[2] = max[1]
                max[1] = max[0]
                max[0] = num
            elif num > max[1]:
                max[2] = max[1]
                max[1] = num
            elif num > max[2]:
                max[2] = num
            print(max)
            print(sum(max))
            print(max[0] + max[1] + max[2])
            break
        if line.strip():
            num = num + int(line)
        else:
            if num > max[0]:
                max[2] = max[1]
                max[1] = max[0]
                max[0] = num
            elif num > max[1]:
                max[2] = max[1]
                max[1] = num
            elif num > max[2]:
                max[2] = num
            num = 0