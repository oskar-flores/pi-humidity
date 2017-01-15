import statsd
import os
import psutil
import RPi.GPIO as GPIO
import Adafruit_DHT as dht


host = os.uname()[1]
cpu = psutil.cpu_percent(interval=1)

client = statsd.StatsClient('statsd', 8125, host)


def setup_pin_40():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(40, GPIO.OUT)
    GPIO.output(40, GPIO.HIGH)


def log_humidity(stadsclient, humidity):
    stadsclient.gauge('lonja.humidity', humidity)


def log_temperature(stadsclient, temperature):
    stadsclient.gauge('lonja.temperature', temperature)


def log_cpu(stadsclient, cpu):
    stadsclient.gauge('cpu.percent', cpu)


def read_sensor():
    h, t = dht.read_retry(dht.DHT22, 20)
    return h, t

setup_pin_40()

while True:

    log_cpu(client, cpu)

    humidity, temperature = read_sensor()

    log_humidity(client, humidity)

    log_temperature(client, temperature)
