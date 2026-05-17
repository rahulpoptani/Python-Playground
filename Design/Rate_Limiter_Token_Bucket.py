import time
import threading

TOKEN = 0

def refill():
    global TOKEN
    while True:
        time.sleep(1)
        if TOKEN < 10:
            TOKEN += 1
            print(f"[refill]  TOKEN = {TOKEN}")

t1 = threading.Thread(target=refill, daemon=True)
t1.start()

while True:
    key = input()
    if key.strip().lower() == "q":
        print("Bye.")
        break
    elif key == "":
        if TOKEN > 0:
            TOKEN -= 1
            print(f"[consume] TOKEN = {TOKEN}")
        else:
            print("[rejected] No tokens left!")