#Load time
load_time=float(input("Enter load time in seconds:\t"))
if load_time<0:
    print("invalid load time")
elif load_time<3 and load_time>0:
    print(f"⚠️ Performance fine:{load_time}")
elif load_time>3:
    print(f"⚠️ Page load too slow:\t{load_time}")
