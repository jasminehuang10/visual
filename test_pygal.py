# 生成数据
from random import randint


class Die():
    """表示一个骰子的类"""

    def __init__(self, num_sides=6):
        """默认骰子为6面"""
        self.num_sides = num_sides

    def roll(self):
        """返回一个介于1和骰子面数之间的数"""
        return randint(1, self.num_sides)
