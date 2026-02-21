import time

try:
    while True:
     current_time = time.strftime("%I:%M:%S %p")
     print(f"Current time: {current_time}",end="\r")
     time.sleep(1)

except KeyboardInterrupt:
    print("\nClock stopped.")