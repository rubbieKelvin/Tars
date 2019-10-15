from tars import tars
import time

while True:
    try:
        tars_ = tars.Tars()
        tars_.run()
    except Exception as e:
        print("error:", e)
    time.sleep(5)
