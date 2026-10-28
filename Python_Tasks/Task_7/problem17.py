# Problem: Separate the Numbers
# HackerRank: https://www.hackerrank.com/challenges/separate-the-numbers/problem

q = int(input().strip())

for _ in range(q):
    s = input().strip()
    answer = None

    for length in range(1, len(s) // 2 + 1):
        first = s[:length]
        if first.startswith("0"):
            continue

        current = first
        expected = int(first) + 1
        while len(current) < len(s):
            current += str(expected)
            expected += 1

        if current == s:
            answer = first
            break

    if answer is None:
        print("NO")
    else:
        print("YES", answer)
