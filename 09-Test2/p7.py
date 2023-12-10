def f(arr):
    counter = 0
    valid = False
    for username in arr:
        if len(username) < 4 or len(username) > 12:
            valid = False
        else:
            for c in username:
                if (c.isalpha() and c.islower()) or c.isdigit() or c == "_":
                    valid = True
                else:
                    valid = False
                    break
        if valid:
            counter+=1
    return counter
        

if __name__ == "__main__":
    print(f(["uek","water_7_x","anna.may","a_b_c_d_e_f"]))

