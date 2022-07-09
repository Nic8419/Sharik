import json

class Player:
    def __init__(self, x, y, step=1):
        self.x = x
        self.y = y
        self.step = step
        self.data = 0
        self.x_x = x
        self.y_y = y
        self.qq = 0
        self.ww = 0

    def moveRight(self):
        self.x = self.x + self.step

    def moveLeft(self):
        self.x = self.x - self.step

    def moveUp(self):
        self.y = self.y - self.step

    def moveDown(self):
        self.y = self.y + self.step

    def old_position(self):
        self.x_x = self.x
        self.y_y = self.y

    def save_game(self):
        self.data = self.y_y, self.x_x, self.qq, self.ww
        with open('data.txt', 'w') as outfile:
            json.dump(self.data, outfile)


    def load_game(self):
        with open('data.txt') as num:
            try:
                data = json.load(num)
                sv = input('Открыть сохраненную игру? y / n ')
                if sv == 'y':
                    self.y, self.x, self.qq, self.ww = data
                else:
                    f = open('data.txt', 'wb')
                    f.close()
            except json.decoder.JSONDecodeError as err:
                print('Сохранений не найдено')


    def right(self):
        print('Шарик нашел правильный пути. Сделайте следующий ход')
    def wall(self):
        print('Шарик ударился о стену. Игра окончена')
    def wrong(self):
        print('Шарик заблудился. Игра окончена')
    def coward(self):
        print('Шарик струсил и убежал. Игра окончена')
    def win(self):
        print('Шарик прошел через все оптимальные ходы - поздравляем с победой')

maze = [
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 0, 1, 1, 1, 1, 2, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 2, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1, 2, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 0, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 0, 0, 0, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 3],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
                     ]


player = Player(0, 1)
player.load_game()

while True:
    player.old_position()
    action = input('Шарик ожидает ход: up / down / left / right ')
    if action == 'up':
        player.moveUp()
    elif action == 'down':
        player.moveDown()
    elif action == 'left':
        player.moveLeft()
    elif action == 'right':
        player.moveRight()
    else:
        continue

    if player.qq == player.y and player.ww == player.x:
        player.coward()
        break

    if maze[player.y][player.x] == 0:
        player.right()
        player.qq = player.y_y
        player.ww = player.x_x

    elif maze[player.y][player.x] == 1:
        player.wall()
        break

    elif maze[player.y][player.x] == 2:
        player.wrong()
        break

    elif maze[player.y][player.x] == 3:
        player.win()
        exit()

save = input('Желаете сохранить игру? y / n ')
if save == 'y':
    player.save_game()
else:
    f = open('data.txt', 'wb')
    f.close()