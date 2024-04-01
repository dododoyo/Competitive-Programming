def convert_time():
    hour, minutes = map(int, input().split(":"))

    if hour == 0:
        return f"12:{minutes:02d} AM"
    elif hour < 12:
        return f"{hour:02d}:{minutes:02d} AM"
    elif hour == 12:
        return f"{hour:02d}:{minutes:02d} PM"
    else:
        return f"{hour-12:02d}:{minutes:02d} PM"


for _ in range(int(input())):
    print(convert_time())
