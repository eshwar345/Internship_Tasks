# Problem: Merge the Tools!
# HackerRank: https://www.hackerrank.com/challenges/merge-the-tools/problem

def merge_the_tools(string, k):
    for start in range(0, len(string), k):
        chunk = string[start:start + k]
        seen = set()
        result = []
        for character in chunk:
            if character not in seen:
                seen.add(character)
                result.append(character)
        print("".join(result))

if __name__ == "__main__":
    string = input().strip()
    k = int(input())
    merge_the_tools(string, k)
