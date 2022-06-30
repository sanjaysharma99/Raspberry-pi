import RPi.GPIO as gpio
from flask import Flask

app=Flask(__name__)

gpio.setmode(gpio.BOARD)
gpio.setup(3,gpio.OUT)
gpio.setup(5,gpio.OUT)
gpio.setup(7,gpio.OUT)
gpio.setup(8,gpio.OUT)

global state1
global state2
global state3
global state4

state1=True
state2=True
state3=True
state4=True

@app.route('/led1')
def fun1():
    global state1
    if state1:
        state1=False
    else:
        state1=True
    gpio.output(3,state1)
    return f'The LED1 Is Set {state1}'
            
@app.route('/led2')
def fun2():
    global state2
    if state2:
        state2=False
    else:
        state2=True
    gpio.output(5,state2)
    return f'The LED1 Is Set {state2}'

@app.route('/led3')
def fun1():
    global state3
    if state3:
        state3=False
    else:
        state3=True
    gpio.output(7,state3)
    return f'The LED1 Is Set {state3}'
    

@app.route('/led4')
def fun1():
    global state4
    if state4:
        state4=False
    else:
        state4=True
    gpio.output(8,state4)
    return f'The LED1 Is Set {state4}'

app.run()

