for x in range(7):
    x = int(input("Enter a number: "))
    if x >= 0:
        result=('X'*x)
    else:
        result=(" ")
with open("numbers.txt", "w", encoding="utf-8") as f:
    for y in result:
        lines = list(result)
        for line in lines:
            f.writelines(lines)
            
          
   
          






    



