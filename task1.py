calculations = [
    {"a": 12, "b": 4, "op": "+"},
    {"a": 25, "b": 10, "op": "-"},
    {"a": 6, "b": 7, "op": "*"},
    {"a": 20, "b": 5, "op": "/"},
    {"a": 15, "b": 0, "op": "/"},
    {"a": 8, "b": 3, "op": "+"}
]

for item in calculations:
    a = item["a"]
    b = item["b"]
    op = item["op"]
    
    if op == "+":
        print(a + b)
    elif op == "-":
        print(a - b)
    elif op == "*":
        print(a * b)
    elif op == "/":
        if b == 0:
            print("Error: You cannot divide by zero")
        else:
            print(a / b)
