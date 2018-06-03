#!/usr/bin/env python3

class SweetPotato:

    def __init__(self):
        self.cookedString = "生的"
        self.cookedLevel = 0
        self.condiments = []
    
    def __str__(self):
        return "地瓜状态: {} {},添加的佐料有: {}".format(self.cookedString, self.cookedLevel, str(self.condiments))

    def cook(self, cooked_time):
        #此处的cookedLevel是指当前所指对象中的属性
        self.cookedLevel += cooked_time

        if self.cookedLevel >=0 and self.cookedLevel < 3:
           self.cookedString = "生的"
        elif self.cookedLevel >=3 and self.cookedLevel < 5:
           self.cookedString = "半生不熟"
        elif self.cookedLevel >=5 and self.cookedLevel < 8:
           self.cookedString = "熟的"
        elif self.cookedLevel >=8:
           self.cookedString = "烤糊了"

    def addCondiments(self, item):
        self.condiments.append(item)        

#创建了一个地瓜对象
digua = SweetPotato()
print(digua)

#开始烤地瓜
digua.cook(1)
print(digua)
digua.cook(1)
print(digua)
digua.addCondiments("大蒜")
digua.cook(1)
print(digua)
digua.cook(1)
digua.addCondiments("番茄酱")
print(digua)
digua.cook(1)
print(digua)
digua.addCondiments("辣椒酱")
digua.cook(1)
print(digua)
