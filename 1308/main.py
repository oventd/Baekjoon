import datetime

xy, xm, xd = map(int, input().split())
yy, ym, yd = map(int, input().split())

start = datetime.date(xy, xm, xd)
end = datetime.date(yy, ym, yd)

year_diff = yy - xy

if year_diff > 1000 or (year_diff == 1000 and (ym, yd) >= (xm, xd)):
    print("gg")
else:
    diff = (end - start).days
    if diff == 0:
        print("D-day")
    else:
        print(f"D-{diff}")
