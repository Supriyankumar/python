def add_greetings(names):
    empty_list = []
    for name in names:
        empty_list.append("Hello, " + name)
    return(empty_list)


print(add_greetings(["Owen", "Max", "Sophie"]))