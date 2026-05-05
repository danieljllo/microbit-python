from microbit import * 
# Servo control: 
# 50 = ~1 millisecond pulse all right 
# 75 = ~1.5 millisecond pulse center 
# 100 = ~2.0 millisecond pulse all left 
pin0.set_analog_period(20)

while True: 
    pin0.write_analog(75)
    display.show(Image.ARROW_N)
    sleep(1000)

    pin0.write_analog(50)
    display.show(Image.ARROW_NE)
    sleep(1000)
    pin0.write_analog(25)
    display.show(Image.ARROW_E)
    sleep(1000)
    
    pin0.write_analog(75)
    display.show(Image.ARROW_N)
    sleep(1000)
    
    pin0.write_analog(100)
    display.show(Image.ARROW_NW)
    sleep(1000)
    pin0.write_analog(125)
    display.show(Image.ARROW_W)
    sleep(1000)
    