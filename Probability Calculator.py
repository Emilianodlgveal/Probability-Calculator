import copy
import random


class Hat:
    def __init__(self, **kwargs):
        self.contents = list()
        for i, v in kwargs.items():
            self.contents.extend(str((i + ' ') * v).split())
        print(self.contents)

    def draw(self, num):
        self.newlist = list()
        try:
            for i in range(num):
                random.shuffle(self.contents)
                self.newlist.append(self.contents.pop())
            return (self.newlist)
        except IndexError:
            return (self.newlist)


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    x = 0
    for i in range(num_experiments):
        n = list()
        copy_hat = copy.deepcopy(hat)
        copy_expected = copy.deepcopy(expected_balls)
        colorsGot = copy_hat.draw(num_balls_drawn)
        for k, v in copy_expected.items():
            n.extend(str((k + ' ')*v).split())
        p = 0
        for color in n:
            if color in colorsGot:
                colorsGot.pop(colorsGot.index(color))
                p += 1
            if p >= 3:
                x += 1
                break
    return (x/num_experiments)

hat = (Hat(blue=3,red=2,green=6))
# print(experiment(hat=hat, expected_balls={"blue":2,"green":1}, num_balls_drawn=4, num_experiments=1000))


# hat = Hat(yellow=5,red=1,green=3,blue=9,test=1)
# print(experiment(hat=hat, expected_balls={"yellow":2,"blue":3,"test":1}, num_balls_drawn=20, num_experiments=100))
