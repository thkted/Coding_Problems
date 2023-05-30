# input
X = int(input())

# main
bin_num = bin(X)[2:]
print(bin_num.count('1'))