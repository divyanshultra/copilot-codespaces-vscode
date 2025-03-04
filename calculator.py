def calculator():
    try:
        expression = input("Enter expression (e.g., 3 + 4): ")
        result = eval(expression)
        print("Result:", result)
    except Exception as e:
        print("Error:", e)

calculator()
