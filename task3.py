calculations = [
    {"a": 12, "b": 4, "op": "+"},
    {"a": 25, "b": 10, "op": "-"},
    {"a": 6, "b": 7, "op": "*"},
    {"a": 20, "b": 5, "op": "/"},
    {"a": 15, "b": 0, "op": "/"},
    {"a": 8, "b": 3, "op": "+"}
]

def calculate(a, b, operation):
    try:
        return operation(a, b)
    except ZeroDivisionError:
        return None

def power(a, b):
    return a ** b

operations_map = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b
}

results = []
for item in calculations:
    op_func = operations_map[item["op"]]
    res = calculate(item["a"], item["b"], op_func)
    results.append(res)

print(results)
