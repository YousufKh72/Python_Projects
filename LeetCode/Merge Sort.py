nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3

p1 = m - 1
print(p1)

p2 = n - 1
print(p2)

p3 = p1 + p2 - 1
print(p3)

while p1 >= 0 and p2 >= 0:
    if nums1[p1] > nums2[p2]:
        nums1[p3] =