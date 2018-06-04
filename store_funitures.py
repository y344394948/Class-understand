#!/usr/bin/env python3

class House():

    def __init__(self, new_area, new_category, new_addr):
        self.area = new_area
        self.category = new_category
        self.addr = new_addr
        self.left_area = new_area #房子剩余面积
        self.contain_items = []   #房子中的家具包括什么...

    def __str__(self):
        massage = '房子的总面积为: {}平方米,可用面积为:{}平方米,户型是:{},地址是:{}'.format(self.area, self.left_area, self.category, self.addr)
        massage += ' 当前房子中的物品有:{}'.format(str(self.contain_items))
        return massage

    def add_item(self, item):    #当针对房子创建了一个对象后，调用该方法时，所传的参数是家具的实例化对象，即item指的就是家具对象 
        self.left_area -= item.area
        self.contain_items.append(item.get_name())

class Funitures():
    
    def __init__(self, new_name, new_area):
        self.name = new_name
        self.area = new_area

    def __str__(self):
        return '{}占用的面积是:{}平方米'.format(self.name, self.area)

    def get_area(self):
        return self.area

    def get_name(self):
        return self.name

#创建一个房子对象，将fangzi指向该对象
fangzi = House(129, "三室一厅", "北京市 朝阳区 长安街 666号")

#创建一个家具对象，将bed指向该对象
bed = Funitures("席梦思", 4)
table = Funitures("电脑桌", 1)
bed2 = Funitures("三人床", 6)

#fangzi调用House类中的add_item方法，并将bed传给该方法
fangzi.add_item(bed)
print(fangzi)

fangzi.add_item(table)
print(fangzi)

fangzi.add_item(bed2)
print(fangzi)
