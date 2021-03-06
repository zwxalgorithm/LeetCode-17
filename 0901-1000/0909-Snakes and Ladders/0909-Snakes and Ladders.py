import collections
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        N = len(board)
        steps = {1: 0}
        Q = collections.deque([1])
        while Q:
            curr = Q.popleft()
            for k in range(1, 7):
                next = curr + k
                if next <= N * N:
                    r = (next - 1) // N
                    c = (next - 1) % N
                    nr = N - 1 - r
                    nc = N - 1 - c if (r & 1) else c
                    if board[nr][nc] != -1:
                        next = board[nr][nc]
                    if next == N * N:
                        return steps[curr] + 1
                    if next not in steps:
                        steps[next] = steps[curr] + 1
                        Q.append(next)
                else:
                    break
        return -1
