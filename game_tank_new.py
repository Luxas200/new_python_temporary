import time
from random import randint

class Tank:
    def __init__(self,
                 position = (5, 5),
                 movement = None,
                 target = None,
                 tank_direction = '<',
                 tank_coordinates = None,
                 tank_hits = 0,
                 tank_misses = 0,
                 tank_count_shoots = 0,
                 tank_shoots_left = 0,
                 tank_shoots_right = 0,
                 tank_shoots_north = 0,
                 tank_shoots_south = 0):
        self.tank_hits = tank_hits
        self.tank_misses = tank_misses
        self.position = position
        self.movement = movement
        self.target = target
        self.tank_direction = tank_direction
        self.tank_coordinates = tank_coordinates
        self.tank_count_shoots = tank_count_shoots
        self.tank_shoots_left = tank_shoots_left
        self.tank_shoots_right = tank_shoots_right
        self.tank_shoots_north = tank_shoots_north
        self.tank_shoots_south = tank_shoots_south

    def generate_target(self):
       while True:
           self.target = (randint(0,9), randint(0,9))
           if self.target != self.position:
            break

    def draw_table(self, bullet = None):
       for i in range(10):
           for y in range(10):
               if i == self.position[0] and y == self.position[1]:
                   print(self.tank_direction, end='')
               elif bullet and i == bullet[0] and y == bullet[1]:
                   print('*', end='')
               elif self.target and i == self.target[0] and y == self.target[1]:
                   print('o', end='')
               else:
                   print('__', end='')
           print()

    def move_tank(self, direction):
        new_position = self.position
        if direction == '<' and self.position[1] > 0:
            new_position = self.position[0], self.position[1] - 1
        elif direction == '>' and self.position[1] < 9:
            new_position = self.position[0], self.position[1] + 1
        elif direction == '^' and self.position[1] > 0:
            new_position = self.position[0] - 1, self.position[1]
        elif direction == 'v' and self.position[1] < 9:
            new_position = self.position[0] + 1, self.position[1]

        if new_position != self.target:
            self.position = new_position
            self.tank_direction = direction

    def turn_left(self):
        if self.tank_direction == '<':
            self.tank_direction = 'v'
        elif self.tank_direction == 'v':
            self.tank_direction = '>'
        elif self.tank_direction == '>':
            self.tank_direction = '^'
        elif self.tank_direction == '^':
            self.tank_direction = '<'

    def turn_right(self):
        if self.tank_direction == '<':
            self.tank_direction = '^'
        elif self.tank_direction == '^':
            self.tank_direction = '>'
        elif self.tank_direction == '>':
            self.tank_direction = 'v'
        elif self.tank_direction == 'v':
            self.tank_direction = '<'

    def shoot(self):
        bullet = None
        self.tank_count_shoots += 1
        if self.tank_direction == '>':
            self.tank_shoots_right += 1
            for i in range(self.position[1] + 1, 10):
                if self.target == (self.position[0], i):
                    bullet = (self.position[0], i)
                    self.tank_hits += 1
                    print('Yeah, you hit the target!')
                    tank.generate_target()
                    break
        elif self.tank_direction == '<':
            self.tank_shoots_left += 1
            for i in range(self.position[1] -1, -1, -1):
                if self.target == (self.position[0], i):
                    bullet = (self.position[0], i)
                    self.tank_hits += 1
                    print('Yeah, you hit the target!')
                    tank.generate_target()
                    break
        elif self.tank_direction == '^':
            self.tank_shoots_north += 1
            for i in range(self.position[0] - 1, -1, -1):
                if self.target == (i, self.position[1]):
                    bullet = (i, self.position[1])
                    self.tank_hits += 1
                    print('Yeah, you hit the target!')
                    tank.generate_target()
                    break
        elif self.tank_direction == 'v':
            self.tank_shoots_south += 1
            for i in range(self.position[0] + 1, 10):
                if self.target == (i, self.position[1]):
                    bullet = (i, self.position[1])
                    self.tank_hits += 1
                    print('Yeah, you hit the target!')
                    tank.generate_target()
                    break

        if not bullet:
            self.tank_misses += 1
            print('Oh no, captain, we missed, lets load the new bullet and try again!')

        tank.draw_table()

        # not working properly, when shoot is missed. Need to be fixed:

        # if 0 < bullet[0] < 10 and 0 <= bullet[1] < 10:
        #     self.draw_table(bullet)
        #     time.sleep(0.9)

    def count_hit_ratio(self):
        if self.tank_count_shoots > 0:
            return (self.tank_hits/self.tank_count_shoots) * 100
        return 0

    def print_statistic(self):
        print(f"""
        Tank direction now: {self.tank_direction} coordinates: x = {self.position[0]}, y = {self.position[1]}
        Shoots made: {self.tank_count_shoots}
        Hits: {self.tank_hits}
        Missed: {self.tank_misses}
        
        Hit ratio: {tank.count_hit_ratio()} %
        
        Shoots right {self.tank_shoots_right} Shoots left {self.tank_shoots_left}
        Shoots north {self.tank_shoots_north} Shoots south {self.tank_shoots_south}
        """)

tank = Tank()

targets_mission = int(input('Here is your mission - enter the number of targets you want to hit: '))

tank.generate_target()
tank.draw_table()
tank.count_hit_ratio()

while True:
    if tank.tank_hits >= targets_mission:
        print(f'Congrats! Mission completed! Your Hit ratio: {tank.count_hit_ratio()} %')
        tank.print_statistic()
        break

    value = input('Enter Tank direction ( > , < , ^ , v ), shoot (s), turn right (e), turn left (q), (i) for stats: (x) to quit ')
    if value == 'x':
        print('Game over! Your mission not completed!')
        tank.print_statistic()
        break

    if value in '><^v':
        tank.move_tank(value)
    elif value == 's':
        tank.shoot()
    elif value == 'e':
        tank.turn_right()
    elif value == 'q':
        tank.turn_left()
    elif value == 'i':
        tank.print_statistic()
    tank.draw_table()


