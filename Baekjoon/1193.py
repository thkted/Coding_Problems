# input
X = int(input())

# main
line = 0
max_num = 0

while X > max_num:
    line += 1
    max_num += line

gap = max_num - X
if line % 2 == 0:
    top = line - gap
    down = gap + 1

else:
    top = gap + 1
    down = line - gap

print('{}/{}'.format(top, down))

