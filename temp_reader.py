import statsd
import os
import psutil

host = os.uname()[1]
cpu = psutil.cpu_percent(interval=1)

client = statsd.StatsClient('statsd', 8125, host)

client.gauge('cpu.percent', cpu)