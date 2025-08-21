n = int(input())
data = []
for _ in range(n):
    data.append(int(input()))

def bs():
    max_num = -1
    for t in range(2, len(data)):
        visited= set() 
        i1 = 0
        i2 = t-1
        while i1 <= i2:
            mid1 = (i1 + i2) //2
            if data[t] - data[mid1] < data[mid1]:
                i2 = mid1 -1
            elif data[t] - data[mid1] >= data[mid1]:
                i3 = i2
                i4 = t
                while i3 <= i4:
                    mid2 = (i3 + i4) //2
                    if data[t] - data[mid2] < data[mid2]:
                        i4 = mid2 -1
                    elif data[t] - data[mid2] >= data[mid2]:
                        i5 = i4
                        i6 = t
                        while i5 <= i6:
                            mid3 = (i5+ i6) // 2
                            if {mid1, mid2, mid3} in visited:
                                break
                            visited.add({mid1, mid2, mid3})
                            if data[mid1]+data[mid2]+data[mid3] == data[t]:
                                if max_num<data[t]:
                                    max_num = data[t]
                            
                            elif data[t] - data[mid3] >= data[mid3]:
                                i5 = mid3 + 1
                            elif data[t] - data[mid3] < data[mid3]:
                                i6 = mid3 -1
                        i3 = mid2 +1
                i1 = mid1 + 1
                                    
        return -1

bs()

# def original_bs(t):
#     start = 0
#     end = len(data)-1
#     while start <= end:
#         mid = (start + end) //2
#         if data[mid] == t:
#             return mid
#         elif data[mid] < t:
#             start = mid +1
#         elif data[mid] > t:
#             end = mid -1
#     return -1