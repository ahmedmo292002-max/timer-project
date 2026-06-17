import time
print("welcome to the promodo timer !")

mins = input("enter your time in minutes: ")
mins = int(mins)

total_seconds = mins * 60
print(total_seconds)

while total_seconds > 0:
    time.sleep(1)
    total_seconds -= 1
    mins = total_seconds // 60
    secs = total_seconds % 60
    clock = f"{mins:02d}:{secs:02d}"
    print(clock,end="\r" )