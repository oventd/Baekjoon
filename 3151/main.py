import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
arr.sort()

count = 0

for i in range(N - 2):
    left, right = i + 1, N - 1
    while left < right:
        s = arr[i] + arr[left] + arr[right]

        if s == 0:
            # left 부터 right 까지 모두 같은 수.
            if arr[left] == arr[right]:
                # k개의 모든 경우의 수 합은 k*(k+1)//2
                count += (right - left + 1) * (right - left) // 2
                break
            else:
                l_count, r_count = 1, 1
                #left부터 같은 인덱스 몇개인지
                while left + 1 < right and arr[left] == arr[left + 1]:
                    l_count += 1
                    left += 1
                #right 부터 같은 인덱스 몇개인지
                while right - 1 > left and arr[right] == arr[right - 1]:
                    r_count += 1
                    right -= 1
                count += l_count * r_count
                left += 1
                right -= 1
        elif s < 0:
            left += 1
        else:
            right -= 1

print(count)
