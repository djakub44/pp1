class Phone:
    def __init__(self,name,brand,color,serial):
        self.name = name
        self.brand = brand
        self.color = color
        self.serial = serial
        self.connected = True

    def GetSerial(self):
        return self.serial
    
    def GetColor(self):
        return self.color
    
    def SendMessage(self,message):
        if self.connected:
            print (f"sent: {message}")
        else:
            print (f"not sent: {message}")

    def PlaneModeON(self):
        self.connected = False

    def PlaneModeOFF(self):
        self.connected = True
    
    def __str__(self):
        return self.name

    
if __name__ == "__main__":
    myPhone = Phone("iVaro","iphone","black","abc12345")

    myPhone.SendMessage("Hello")

    myPhone.PlaneModeON()
    myPhone.SendMessage("Hello")
    myPhone.PlaneModeOFF()
    print(myPhone)