# Save on CPX/CPB as code.py
# Blinks the top right RED LED
import board
import digitalio
import analogio
import time

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT
         
while True:
        led.value = True
        time.sleep(1)
        led.value = False
        time.sleep(1)
    
main()
