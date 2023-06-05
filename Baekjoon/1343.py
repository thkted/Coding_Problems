# input
board = input()

# main
# ans = ''
# start, count = 0, 0
# for idx, s in enumerate(board):
#     if s == 'X':
#         count += 1
#
#     if s == '.' or (idx == (len(board) - 1) and count > 0):
#         if count % 2:
#             ans = '-1'
#             break
#
#         while True:
#             if count == 0:
#                 break
#
#             if count // 4:
#                 ans += 'AAAA' * (count // 4)
#                 count -= 4 * (count // 4)
#
#             if count // 2:
#                 ans += 'BB' * (count // 2)
#                 count -= 2 * (count // 2)
#
#         if s == '.':
#             ans += '.'
#
# print(ans)

# source code
board = board.replace('XXXX', 'AAAA')
board = board.replace('XX', 'BB')

if 'X' in board:
    print(-1)
else:
    print(board)