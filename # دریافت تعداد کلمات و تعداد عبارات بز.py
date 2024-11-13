n, m = map(int, input().split())
responses = {}

for _ in range(n):
    word, reply = input().split()
    responses[word] = reply

words = input().split()

result = []
for word in words:
    if word in responses:
        result.append(f"{responses[word]} kachal!")
    else:
        result.append("kachal!")

print(" ".join(result))



