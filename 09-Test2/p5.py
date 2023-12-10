import re

def f(start,end):
    with open("data.txt","r",encoding="utf8") as file:
        pattern = "\\b" + start + "\w+" + end + "\\b"
        
        print(pattern)
        searchstr = file.read()
        
        result = re.findall(pattern,searchstr)

        return len(result)
    
if __name__ == "__main__":
    print(f("w","d"))