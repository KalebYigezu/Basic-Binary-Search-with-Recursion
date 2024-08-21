def binary_search(l, low, high, s):
    if low <= high:
        mid = (low + high) // 2
        if l[mid] == s:
            print(s, " is found at position", mid + 1)
        elif l[mid] > s:
            binary_search(l, low, mid - 1, s)
        else:
            binary_search(l, mid + 1, high, s)
    else:
        print(s, " is not found")


l = []
n = int(input("Enter a number of elements to be inserted: "))
print("Enter ", n, " elements :")
for i in range(n):
    l.append(int(input()))
l.sort()
print("The sorted list is:", l)
s = int(input("Enter a number to be searched for : "))

low = 0
high = len(l) - 1

binary_search(l, low, high, s)

