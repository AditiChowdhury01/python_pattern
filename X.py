for row in range(7):                                      
   for col in range(5):
        if(col==0 and row !=2 and row !=3 and row !=4) or (col==4 and row !=2 and row !=3 and row !=4) or (row ==2 and (col>=1 and col<4) and col!=2) or (row ==4 and ( (col>=1 and col<4) and col!=2) or (col==2 and row ==3)):
              print("*",end = ' ')
        else:           
          print(end= "  ")    
   print()
