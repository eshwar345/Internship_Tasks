# Problem: Super Reduced String
# HackerRank: https://www.hackerrank.com/challenges/reduced-string/problem

s = input().strip()
stack = []

for character in s:
    if stack and stack[-1] == character:
        stack.pop()
    else:
        stack.append(character)

result = "".join(stack)
print(result if result else "Empty String")
