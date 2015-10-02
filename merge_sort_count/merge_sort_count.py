f = open("IntegerArray.txt", "r")
array = []
for line in f:
  array.append(int(line))
f.close()

def icount(ar, count=0):
    if len(ar)<2: return ar, count
    cut = len(ar)/2
    left, lcount = icount(ar[:cut], count)
    right, rcount = icount(ar[cut:], count)
    return merge_sort(left, right, lcount + rcount)

def merge_sort(left, right, count):
    cork = []
    while left and right:
        ck = left if left[0] <= right[0] else right
        cork.append(ck.pop(0))
        if ck == right: count += len(left)
    cork.extend(left if left else right)
    return cork, count

sorted_a, count = icount(array)
print count
