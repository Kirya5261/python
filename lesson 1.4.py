max_dig = 0
dig = int(input())
while dig // 10 != 0:
    new_dig = dig % 10
    if new_dig > max_dig:
        max_dig = new_dig
    dig = dig // 10
print(max_dig)