# bounce.py
#
# Exercise 1.5
max_bounce_num = 10
current_height = 100 #metres
bounce = 1

while bounce <= max_bounce_num:
    print(bounce, end=' ')
    print(round(current_height * 3/5, 4))
    bounce += 1
    current_height *= 3/5