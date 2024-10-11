def join_calculator():
    import math
    YA = float(input('enter Y component of Y coordinate:'))
    XA = float(input('enter X component of X coordinate:'))
    YB = float(input('enter Y component of Y coordinate:'))
    XB = float(input('enter X component of X coordinate:'))
    YD = YB - YA
    XD = XB - XA
    D = math.sqrt(YD ** 2 + XD ** 2)
    F = YD / XD
    T = math.degrees(math.atan(F))
    Q1 = T
    Q2 = 180 - T
    Q3 = 180 + T
    Q4 = 360 - T

    if XD > 0 and YD > 0:
        print(f"join AB: {D} m, {Q1} degrees")
    elif XD < 0 and YD > 0:
        print(f"join AB: {D} m, {Q2} degrees")
    elif XD < 0 and YD < 0:
        print(f"join AB: {D} m, {Q3} degrees")
    else:
        print(f"join AB: {D} m, {Q4} degrees")
join_calculator()
