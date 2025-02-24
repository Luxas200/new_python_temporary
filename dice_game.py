import random

class Dice:
    def __init__(self, dice_side):
        self.dice_side = dice_side

    def __len__(self):
        return len(self.dice_side)

    def __getitem__(self, index):
        return self.dice_side[index]

    def get_dices_side_number(self):
        dice_side_input = int(input('Enter dice sides 1-100 '))
        if 1 <= dice_side_input <= 100:
            print(f' You entered: {dice_side_input}')
            self.dice_side = list(range(1, dice_side_input + 1))
            return self.dice_side
        else:
            print('WRONG NUMBER! Try again! Please enter valid number <<1 - 100>>')
            return self.get_dices_side_number()

    def throw_dice(self):
        return random.choice(self.dice_side)

class Game(Dice):
    def __init__(self, dice_quantity, dice_side):
        super().__init__(dice_side)
        self.dice_quantity = dice_quantity
        self.game_history = []
        self.result = []
        self.player_count = 0

    def get_user_dices_quantity(self):
        dice_quantity_input = int(input('Enter how many dices you want to throw: 1-5 '))
        if 1 <= dice_quantity_input <= 5:
            print(f' Here is yours  {dice_quantity_input} dices. Please throw!')
            self.dice_quantity = dice_quantity_input
            return self.dice_quantity
        else:
            print('WRONG NUMBER! Try again! Please enter valid number <<1 - 5>>  ')
            return self.get_user_dices_quantity()

    def throw_all_dices(self):
        self.result = []
        for _ in range(self.dice_quantity):
            result = self.throw_dice()
            self.result.append(result)
        return self.result

    def play_game(self, player_name):
        self.get_user_dices_quantity()
        self.throw_all_dices()
        total_sum = sum(self.result)
        self.game_history.append({
            'player': player_name,
            'results': self.result,
            'total points': total_sum
        })
        self.player_count += 1
        print(f'Results of {self.dice_quantity} dice throws: {self.result} and final result is: {total_sum}')
        return total_sum

    def show_game_history(self):
        print('Game history:')
        for every_entry in self.game_history:
            print(f'Player: {every_entry['player']}, Total: {every_entry['total points']}')

if __name__ == '__main__':
    pass

players_in_game = int(input('Enter how many players will play: '))

game = None

while players_in_game > 0:
    player_name = input('Please enter your name: ')

    if game is None:
        dice = Dice([])
        dice_side = dice.get_dices_side_number()
        game = Game(0, dice_side)

    game.play_game(player_name)
    players_in_game -= 1

game.show_game_history()
