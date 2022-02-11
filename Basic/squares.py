# squares = []
# for value in range(1, 11):
#     square = value**2
#     squares.append(square)
#
# print(squares)

squares = [value**2 for value in range(1, 11)]
print(squares)

print(squares[-3:-1]) #打牌输第三个取到最后一个[-3:]
#[-3:-1] 取不到最后一个

