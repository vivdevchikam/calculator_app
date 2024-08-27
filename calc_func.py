# addition

def do_addition(a, b):
  return a + b

# subtraction

def do_subtraction(a, b):
  return a - b


def do_division(a, b):
  try:
    return a / b
  except ZeroDivisionError as e:
    return "Cannot divide by zero"