with open('Day1.txt') as f:
    max = 0
    num = 0
    while True:
        line = f.readline()
        if not line:
            if num > max:
                max = num
            print(max)
            break
        if line.strip():
            num = num + int(line)
        else:
            if num > max:
                max = num
            num = 0