for row in range(7):                                       
   for col in range(5):
        if(col==0 and (row ==1 or row ==2) and row !=0) or (row ==0 and col>0 and col<4) or (row ==3 and col>0 and col<4)or (col==4 and (row ==4 or row ==5))or (row ==6 and col >0 and col <4) :
              print("*",end = ' ')
        else:           
          print(end= "  ")    
   print()
