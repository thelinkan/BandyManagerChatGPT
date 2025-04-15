import math

for x in range(20):
    for y in range(20):
        distance = round(math.sqrt((abs((20+x) - 30)**2 + 
                                    ((80+y) - 100)**2)),3)
        angle = round(math.degrees(math.atan2(abs((20+x) - 30), (80+y) - 100)),3)
        print(f"{20+x} - {80+y}: {distance}/{angle}")