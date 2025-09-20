import sys
N, m, M, T, R = map(int, input().split())
beat = m
time = 0
T_time = 0
if m + T > M:
    print(-1)
    sys.exit()
while T_time < N:
    if m <= beat and beat+T <= M:
        beat += T
        T_time += 1
    else:
        if m > beat-R:
            beat = m
        else:
            beat -= R
    time += 1
print(time)

