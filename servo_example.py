import board, pwmio, time
from adafruit_motor import servo

pwm = pwmio.PWMOut(board.GP12, frequency=50)
my_servo = servo.Servo(pwm)

while True:

    my_servo.angle = 0
    time.sleep(1)

    my_servo.angle = 90
    time.sleep(1)

    my_servo.angle = 180
    time.sleep(1)
