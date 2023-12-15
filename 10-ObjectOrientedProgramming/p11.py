class TV:
    def __init__(self,brand):
        self.brand = brand
        self.is_on = False
    
    def show_status(self):
        if self.is_on:
            print( "TV is ON")
        else:
            print( "TV is OFF")
    
    def turn_on(self):
        self.is_on = True
    
    def turn_off(self):
        self.is_on = False

if __name__ == "__main__":
    myTV = TV("Samsung")
    print(myTV.brand)

    myTV.show_status()
    myTV.turn_on()
    myTV.show_status()
    myTV.turn_off()
    myTV.show_status()