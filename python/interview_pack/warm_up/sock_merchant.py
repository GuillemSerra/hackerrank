from collections import Counter

socks = [1, 2, 2, 1, 1, 3, 5, 1, 2]
n_socks_by_color = Counter(socks)
total_pairs = 0
for color, n in n_socks_by_color.items():
    if n % 2 == 0:
        total_pairs += int(n / 2)
    else:
        total_pairs += int((n - 1) / 2)
print(total_pairs)
