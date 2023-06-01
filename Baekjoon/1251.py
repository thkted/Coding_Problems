# input
word = input()

# function
def find(idx_arr, count):
    if count == 3:
        s1 = word[:idx_arr[1]]
        s2 = word[idx_arr[1]:idx_arr[2]]
        s3 = word[idx_arr[2]:]
        s = s1[::-1] + s2[::-1] + s3[::-1]
        temp.append(s)
        return

    for i in range(len(word)):
        if idx_arr:
            if i > idx_arr[-1]:
                idx_arr.append(i)
                find(idx_arr, count + 1)
                idx_arr.pop()

        else:
            idx_arr.append(i)
            find(idx_arr, count + 1)
            idx_arr.pop()


# main
temp = []
find([], 0)
temp.sort()
print(temp[0])