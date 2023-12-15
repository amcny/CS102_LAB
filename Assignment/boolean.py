a = bool(input("Enter the value for a: "))
b = bool(input("Enter the value for b: "))
def logical_and(a, b):
  if a and b:
    return True
  else:
    return False
def logical_or(a, b):
  if a or b:
    return True
  else:
    return False
print("The result of Logical AND is", logical_and(a, b))
print("The result of Logical OR is", logical_or(a, b))