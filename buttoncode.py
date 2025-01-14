# Save on CPX/CPB as code.py
# Blinks the top right RED LED
import board
import digitalio
import time

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

goat_button_B = digitalio.DigitalInOut(board.BUTTON_B)
goat_button_B.direction = digitalio.Direction.INPUT
goat_button_B.pull = digitalio.Pull.DOWN

print(dir(goat_button_B))  
print("Button_B Input/Output Example")

while True:
    led.value = goat_button_B.value
    print(goat_button_B.value)
    time.sleep(.2)
main()