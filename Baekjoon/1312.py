# input
A, B, N = map(int, input().split())

# function (by myself..)
# def divide(a, b):
#     if a//b:
#         a -= b * (a//b)
#
#     arr = []
#     count = 0
#     while True:
#         if count >= N:
#             print(arr[N - 1])
#             break
#
#         if a == 0:
#             print(0)
#             break
#
#         index = 0
#         while a < b:
#             if index >= 1:
#                 count += 1
#                 arr.append(0)
#             a *= 10
#             index += 1
#
#         arr.append(a // b)
#         a = a % b
#         count += 1
#
# # main
# divide(A, B)

# source code
for i in range(N):
    A = (A % B) * 10
    result = A // B
print(result)