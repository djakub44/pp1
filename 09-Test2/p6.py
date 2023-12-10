def f(years,course):
    import json
    import math
    counter = 0
    score = 0
    with open("data.json","r") as file:
        file_content = json.load(file)
    for person in file_content:
        if person["age"] >= years:
            for coursename in person["studies"]["courses"]:
                if coursename["name"] == course:
                    for i in range(len(coursename["grades"])):
                        score += coursename["grades"][i]
                    score = score/len(coursename["grades"])
                    if score >=4:
                        counter += 1
    return counter

if __name__ == "__main__":
    print(f(21, "statistics"))



