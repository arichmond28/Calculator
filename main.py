def main():
  user_input1 = input("Enter a number: ")
  operation = input("Enter an operation (Plus, Minus, Multiply, Divide): ")
  user_input2 = input("Enter another number: ")
  if operation == "Plus":
    print(int(user_input1) + int(user_input2))
  elif operation == "Minus":
    print(int(user_input1) - int(user_input2))
  elif operation == "Multiply":
    print(int(user_input1) * int(user_input2))
  elif operation == "Divide":
    print(int(user_input1) / int(user_input2))  
  else:
    print("Invalid operation")
main()  