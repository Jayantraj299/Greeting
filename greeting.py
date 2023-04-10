import time
time = time.strftime('%H:%M')

if time >= "24:00":
    print(time,"Go to Sleep")
elif time >= "21:00":
    print(time,"Good Night")
elif time >= "18:00":
    print(time,"Good Evening")
elif time >= "12:00":
    print(time,"Good afternoon")
elif time >= "06:00":
    print(time,"Good Morning")