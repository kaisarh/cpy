import pwmio, board, time
from adafruit_motor import motor

pwm_a = pwmio.PWMOut(board.GP8, frequency=50)
pwm_b = pwmio.PWMOut(board.GP9, frequency=50)

motor1 = motor.DCMotor(pwm_a, pwm_b)

def set_motor(throttle):
    motor1.throttle = throttle
    print("throttle:", throttle)

while True:
    set_motor(0.5)
    time.sleep(1)
