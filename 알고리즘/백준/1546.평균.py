# 평균 구하기 쉽자너

N = int(input())
record = list(map(int, input().split()))
# print(record)

max_record = max(record)
# print(max_record)

new_record = []
for i in record:
    new_record.append((i/max_record)*100)

print(sum(new_record)/len(new_record))
