#!/usr/bin/env python3

class Cat:  #定义了一个Cat类
    """定义了一个Cat类"""
 
    #初始化对象
    def __init__(self, new_name,new_age):
        self.name = new_name
        self.age = new_age
    
    #将对象转化为描述信息
    def __str__(self):
        return '{}的年龄是: {}'.format(self.name, self.age)

    #方法
    def eat(self):  
        print("猫在吃鱼...")
    def drink(self):
        print("猫在喝水...")
    def introduce(self):
        print('{}的年龄是: {}'.format(self.name, self.age))  #self变量，用来传递当前对象，谁调用该方法，此时self就是谁

#创建一个对象
tom = Cat("汤姆", 40)  #调用Cat()即创建了一个新的对象，返回对象的引用，tom指向该对象tom，只要创建了一个对象，则该对象就拥有该类中的所有属性和方法

#调用tom指向的对象中的方法
#tom.eat() 
#tom.drink()

#给tom指向的对象添加两个属性
#tom.name = "汤姆" #tom指向了哪个对象，所添加的属性就往哪个对象中添加
#tom.age = 40

#获取属性的第一种方式
#print('{%s}的年龄是: {}'.format(tom.name, tom.age))

#获取属性的第二种方式
#tom.introduce()

lanmao = Cat("蓝猫", 10)
#lanmao.name = "蓝猫"
#lanmao.age = 10
#lanmao.introduce()


print(tom)
print(lanmao)
