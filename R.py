for row in range(7):                                      
 for col in range(5):
      if(col==0) or ((row ==0 or row ==3)and col!=4) or (col==4 and (row==1 or row ==2 or row ==6) or(row ==4 and col==2) or((row ==5 and col==3))):
            print("*",end = ' ')
      else:           
        print(end= "  ")    
 print()