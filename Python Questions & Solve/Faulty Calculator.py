# Faulty Calculator
# Wrong operations-> 45*3=555,56+9=77,56/6=4

print("Enter first number: ")
n1 = int(input())
print("Enter the second number: ")
n2 = int(input())
print("Which operation do you want? " +
      "\n+ -> Addition\n- -> Subtraction\n* -> Multiplication\n/ -> Division\n% -> Modulus")
n3 = input()
if n1 == 45 and n2 == 3 and n3 == "*":
    print("45*3=555")
elif n1 == 56 and n2 == 9 and n3 == "+":
    print("56+9=77")
elif n1 == 56 and n2 == 6 and n3 == "/":
    print("56/6=4")
elif n3 == "*":
    print(n1, "*", n2, "=", (n1*n2))
elif n3 == "+":
    print(n1, "+", n2, "=", (n1+n2))
elif n3 == "/":
    print(n1, "/", n2, "=", (n1/n2))
elif n3 == "-":
    print(n1, "-", n2, "=", (n1-n2))
elif n3 == "%":
    print(n1, "%", n2, "=", (n1 % n2))
else:
    print("Error!")
