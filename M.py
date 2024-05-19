
for row in range(7):                                       
   for col in range(5):
        if(col==0 or col==4) or ( (col==1 or col==3 and col!=2) and row ==2 ) or (col==2 and row ==3):
          print("*",end = ' ')
        else:           
          print(end= "  ")    
   print()