da = list(map(int, input().split()))
# print(da)
if da == sorted(da):
    print('ascending')

elif da == sorted(da, reverse=True):
    print('descending')

else:
    print('mixed')
