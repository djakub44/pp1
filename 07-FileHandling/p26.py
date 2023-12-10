import re

message = "To be, or not to be, that is the question"

arr = re.findall("[aeiouy]",message)
print (arr)
print (len(arr))
arr2 = ["d","a"]
print (len(arr2))
