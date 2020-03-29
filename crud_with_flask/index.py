class bick():
    count=0

    def __init__(self,brand):
        self.brand=brand
        self.id=bick.count
        bick.count +=1
