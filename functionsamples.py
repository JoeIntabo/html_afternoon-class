def greetings(name, message="Hello"):
    print(name + " " + message)


greetings("Joe")
greetings("Erick", "Mambo")


def maxvalue(a, b, c, d, e, f, g):
    return max(a, b, c, d, e, f, g)


myanswer = maxvalue(5, 34, 1, 89, 345, 0, 10)
print(myanswer)


def minvalue(a, b, c, d, e, f, g):
    return min(a, b, c, d, e, f, g)


myanswer = minvalue(5, 34, 1, 89, 345, 0, 10)
print(myanswer)


def sortedvalue(a, b, c, d, e, f, g):
    return sorted(a, b, c, d, e, f, g)


my_answers = sortedvalue(5, 34, 1, 89, 345, 0, 10)
print(my_answers)
