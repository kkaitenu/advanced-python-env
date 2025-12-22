from collections import Counter

items = input().split()

# 1. Count purchases
counts = Counter(items)

print("Purchase frequency:")
for item, cnt in counts.items():
    print(f"{item}: {cnt}")

# 2. Most frequently purchased item
most_popular = counts.most_common(1)[0][0]
print("Most popular item:", most_popular)

# 3. Items purchased exactly once
once = [item for item, cnt in counts.items() if cnt == 1]
print("Purchased once:", " ".join(once))

# 4. Sort by descending frequency
print("Sorted by frequency:")
for item, cnt in counts.most_common():
    print(item, cnt)