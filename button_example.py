import board, time
import digitalio

btnA = digitalio.DigitalInOut(board.GP20)
btnA.direction = digitalio.Direction.INPUT
btnA.pull = digitalio.Pull.UP

while True:

    if not btnA.value:
        print("btnA is down")
 
    else:
        print("btnA is up")

    time.sleep(1)
