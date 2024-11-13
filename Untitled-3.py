def find_winner(n):
    if n == 1:
        return 1
    else:
        return (find_winner(n - 1) + 2) % n + 1

n = int(input())

print(find_winner(n))
