def calculate_love(name1, name2):
    name = name1 + name2

    t = name.count("t")
    r = name.count("r")
    u = name.count("u")
    e = name.count("e")

    first_digit = t+r+u+e

    l = name.count("l")
    o = name.count("o")
    v = name.count("v")
    e = name.count("e")

    second_digit = l+o+v+e

    print(f"Love score is : {int(str(first_digit)+str(second_digit))}")

calculate_love(input("Enter name 1 : ").lower(), input("Enter name 2 : ").lower())