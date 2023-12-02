class Cube:
    def __init__(self,r,g,b):
        self.r = r
        self.g = g
        self.b = b
    def __str__(self) -> str:
        return str((self.r,self.g,self.b))
    def __repr__(self):
        return str((self.r,self.g,self.b))
    def check(self,other):
        return (self.r <= other.r and self.g <= other.g and self.b <= other.b)

def parse(line):
    colors = ['red','green','blue']
    values = [0]*3
    # 3 green, 12 blue, 3 red
    for seq in line.split(','):
        for i, color in enumerate(colors):
            if color in seq:
                values[i] += int(seq.split()[0])
    return Cube(*values)
def main():
    total = Cube(12,13,14)
    p1 = 0
    with open("input.txt") as f:
        data = f.read().splitlines()
    for game_num, line in enumerate(data):
        game_num += 1
        _, seq = line.split(':')
        sets = []
        for l in seq.split(';'):
            sets.append(parse(l))
        if all(s.check(total) for s in sets):
            p1 += game_num
    return p1

    # print(parse('3 green, 12 blue, 3 red'))

print(main())