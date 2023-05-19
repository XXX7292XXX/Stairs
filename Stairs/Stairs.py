x, y = 0, 0
s2, s4 = [], []
n = int(input())
l = [n for n in input().split()]

s1 = list(set(l))  # Create a list without duplicate elements
for i in range(len(s1)):
    s2.append(l.count(s1[i]))  # Fill the described list with the count of occurrences of each element

print("---" * len(l))  # for convenient output

s3 = list(sorted(s2))
for i in range(len(s3)):
    for j in range(len(s2)):
        if s3[i] == s2[j]:
            s4.append(s1[j])
s2 = []
for i in s4:
    if i not in s2:
        s2.append(i)  # Sorting for ladder-like output

for i in range(len(s1)):
    print(str(s2[i]) * s3[i])  # ladder-like output

for i in range(len(s2)):  # Count jumps
    if s3[i] == s3[i - 1]:
        x -= 1
    x += 1

s3.reverse()
for i in range(len(s3)):  # Count steps to the left
    if s3[i - 1] - s3[i] > 1:
        y += (s3[i - 1] - s3[i]) - 1

print("Number of jumps =", x)
print("Number of steps =", y)
