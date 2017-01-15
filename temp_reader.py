import statsd
import os
import psutil
import RPi.GPIO as GPIO


host = os.uname()[1]
cpu = psutil.cpu_percent(interval=1)

client = statsd.StatsClient('statsd', 8125, host)

client.gauge('cpu.percent', cpu)


def setup_pin_40():
    GPIO.setmode(GPIO.board)
    GPIO.setup(40, GPIO.OUT)
    GPIO.output(40, GPIO.HIGH)


def send_humidity(stadsclient, humidity):
    stadsclient.gauge('lonja.humidity', humidity)


def send_temperature(stadsclient, temperature):
    stadsclient.gauge('lonja.temperature',temperature)
