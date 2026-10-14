calculations = [
    {"a": 12, "b": 4, "op": "+"},
    {"a": 25, "b": 10, "op": "-"},
    {"a": 6, "b": 7, "op": "*"},
    {"a": 20, "b": 5, "op": "/"},
    {"a": 15, "b": 0, "op": "/"},
    {"a": 8, "b": 3, "op": "+"}
]

operations = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b
}

filtered_calculations = filter(lambda x: not (x["op"] == "/" and x["b"] == 0), calculations)
results = list(map(lambda x: operations[x["op"]](x["a"], x["b"]), filtered_calculations))

print(results)
