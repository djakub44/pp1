def f(d):
    avg = 0
    counter = 0
    for key in d:
        avg += d[key]
    avg = avg/len(d)

    for key in d:
        if d[key] > avg:
            counter+=1
    return counter


if __name__ == "__main__":
    print(f({"LO231":150,"BA787":120,"NZ15":30}))
    print(f({"LO231":150,"BA787":20,"NZ15":30}) )