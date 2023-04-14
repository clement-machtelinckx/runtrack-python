def calcule(num1, operator, num2):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2 
    elif operator == "*":
        return num1 * num2 
    elif operator == "/":
        return num1 / num2 
    else: 
        print("error")
    
    
print(calcule (20,"+",20))
print(calcule (20,"-",20))
print(calcule (20,"*",20))
print(calcule (20,"/",20))






