# Problem: Caesar Cipher
# HackerRank: https://www.hackerrank.com/challenges/caesar-cipher-1/problem

n = int(input().strip())
s = input().strip()
k = int(input().strip()) % 26

result = []
for character in s:
    if "a" <= character <= "z":
        result.append(chr((ord(character) - ord("a") + k) % 26 + ord("a")))
    elif "A" <= character <= "Z":
        result.append(chr((ord(character) - ord("A") + k) % 26 + ord("A")))
    else:
        result.append(character)

print("".join(result))
