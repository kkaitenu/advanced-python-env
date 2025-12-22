from collections import Counter

s1 = input().strip()
s2 = input().strip()

if Counter(s1) == Counter(s2):
    print("YES")
else:
    print("NO")