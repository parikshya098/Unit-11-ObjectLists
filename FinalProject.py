class Sketch:
    def __init__(self, size) -> None:
        self.size = size
        self.xpos = 0
        self.ypos = 0
        self.direction = 'U'
        self.pen = 'U'
        self.canvas = [[' ' for x in range(size)]  for x in range(size)]
 
    def printsketch(self):
        print('+' + '-'  * self.size + '+')
        for row in reversed(self.canvas):
            print("|", end='')
            for item in row:
                print(item, end='')
            print("|", end='')
            print()
        print('+' + '-'  * self.size + '+')
 
    def penup(self):
        self.pen = 'U'
 
    def pendown(self):
        self.pen = 'D'
 
    def turnleft(self):
        if self.direction == 'U':
            self.direction = 'L'
        elif self.direction == 'L':
            self.direction = 'D'
        elif self.direction == 'D':
            self.direction = 'R'
        elif self.direction == 'R':
            self.direction = 'U'
 
    def turnright(self):
        if self.direction == 'U':
            self.direction = 'R'
        elif self.direction == 'R':
            self.direction = 'D'
        elif self.direction == 'D':
            self.direction = 'L'
        elif self.direction == 'L':
            self.direction = 'U'
 
    def move(self, distance):
        dx = 0
        dy = 0
        if self.direction == 'U':
            dx = 1
        elif self.direction == 'D':
            dx = -1
        elif self.direction == 'L':
            dy = -1
        elif self.direction == 'R':
            dy = 1
 
        for step in range(distance):
            if self.pen == 'D':
                self.canvas[self.xpos][self .ypos] = '*'
            self.xpos += dx
            self.ypos += dy
def main():
    file = open('Cshape.txt', 'r')
    sketch = Sketch(20)
    while True:
        line = file.readline()
        if not line:
            break
        words = line.split(',')
        words = [int(word) for word in words]
        if len(words) == 2:
            sketch.move(words[1])
        elif words[0] == 1:
            sketch.penup()
        elif words[0] == 2:
            sketch.pendown()
        elif words[0] == 3:
            sketch.turnright()
        elif words[0] == 4:
            sketch.turnleft()
        elif words[0] == 6:
            sketch.printsketch()
    print('X = {}  Y = {}  Direction = {}'.format(sketch.xpos, sketch.ypos, sketch.direction))

main()