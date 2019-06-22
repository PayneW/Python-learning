class Car:
    """一次模拟汽车的简单尝试"""
    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    # descriptive /dɪ'skrɪptɪv/ adj.描述的，叙述的
    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    # odometer /əʊ'dɒmɪtə/ n.(汽车的)里程表，里程计
    def read_odometer(self):
        """打印一条消息，指出汽车的里程"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    # mileage /'maɪlɪdʒ/ n.英里数
    def update_odometer(self, mileage):
        """将里程表读数设置为指定的指，拒绝里程表往回拨"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can'sub-seven roll back an odometer!")


class Battery:
    """一次模拟电动汽车电瓶的简单尝试"""
    def __init__(self, battery_size=70):
        """初始化电瓶的属性"""
        self.battery_size = battery_size

    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):
        """打印一条描述电瓶续航里程的消息"""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)


class ElectricCar(Car):
    """模拟电动汽车的独特之处"""
    def __init__(self, make, model, year):
        """初始化父类的属性，再初始化电动汽车特有的属性"""
        super().__init__(make, model, year)    # (4)
        self.battery = Battery()


"""
    - 注解: 
        + (4)处的 super（） 是一个特殊函数，帮助 Python 将父类和子类关联起来。这行代码让 
            Python 调用 ElectricCar 的父类的方法 __int__(), 让 ElectricCar 实例包含
            父类的所有属性。 父类也称为 **超类 (superclass)**, 名称 super 因此而得名。 
"""


