def f(subjects):
    score = 0
    counter = 0
    scores = {}
    maxkey = ""
    maxscore = 0
    for key in subjects:
        for i in range(len(subjects[key])):
            score += subjects[key][i]
            counter += 1
        score = score/counter
        scores[key] = score
        counter = 0
        score = 0
    for key in scores:
        if scores[key] > maxscore:
            maxkey = key
            maxscore = scores[key]
    return maxkey


if __name__ == "__main__":
    print(f({"math":[3,4,4],"geo":[5,4,4,4],"comp":[5,4]}) )
    print(f({"math":[5,6,6],"geo":[5,4,4,4],"comp":[5,4]}) )