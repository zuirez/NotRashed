def love_count(name):
    l = o = v = e = 0

    for letter in name:
        if letter == "l":
            l += 1
        elif letter == "o":
            o += 1
        elif letter == "v":
            v += 1
        elif letter == "e":
            e += 1
    sum = l+o+v+e
    return sum

def true_count(name):
    t = r = u = e = 0

    for letter in name:
        if letter == "t":
            t += 1
        elif letter == "r":
            r += 1
        elif letter == "u":
            u += 1
        elif letter == "e":
            e += 1
    sum = t+r+u+e
    return sum

def calculate_love(name1, name2):
    true_sum1 = true_count(name1)
    true_sum2 = true_count(name2)
    true_sum = str(true_sum1 + true_sum2)

    love_sum1 = love_count(name1)
    love_sum2 = love_count(name2)
    love_sum = str(love_sum1 + love_sum2)

    love = true_sum + love_sum

    print(f"Love score : {love}")

calculate_love(input("Enter 1st persons name : ").lower(), input("Enter 2nd persons name : ").lower())
