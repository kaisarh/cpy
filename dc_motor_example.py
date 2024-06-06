import time
import board
import pwmio
from adafruit_motor import motor

PWM_PIN_A = board.GP8
PWM_PIN_B = board.GP9

pwm_a = pwmio.PWMOut(PWM_PIN_A, frequency=50)
pwm_b = pwmio.PWMOut(PWM_PIN_B, frequency=50)
motor1 = motor.DCMotor(pwm_a, pwm_b)

def set_motor(throttle):
    motor1.throttle = throttle
    print("throttle:", throttle)

while True:
    set_motor(0.5)
    time.sleep(1)
