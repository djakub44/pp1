arr = [2,3,7,5,4]

print(arr)
print(len(arr))
print(arr[0])
print(arr[1])
print(arr[-1])
print(arr[len(arr)-2])
print(arr[0]+arr[-1])
print (arr[len(arr)//2])

y = ""
for x in range (len(arr)):
    y += str(arr[x])
    if x !=len(arr)-1:
        y += " "
print(y)
