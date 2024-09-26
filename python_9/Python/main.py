import Queue.simple as sq
import Queue.circular as cq
import Queue.doubleEnded as dq
simpleque=[]
circularque=[]
doublque=[]
rear=0
front=-1
while(True):
    print("1:simple Queue")
    print("2:Circular Queue")
    print("3:Double-Ended Queue")
    choice=int(input("Enter your choice:"))

    if(choice==1):
       

        while(True):
           print("\n1:Inset ")
           print("2:Delete")
           print("3:Display")
           print("4:Exit")
           c=int(input("Enter your choice:"))
           if(c==1):
               val=int(input("Enter value:"))
               sq.enqueue(simpleque,val)
           elif(c==2):
               print("Remove Element:",sq.dequeue(simpleque))
           elif(c==3):
              sq.display(simpleque)
           elif(c==4):
               break
           else:
               print("Enter valid input")
    elif(choice==2):
     
         size=int(input("Enter size of Queue:"))
         circularque=cq.circular_queue(circularque,size)
         while(True):
           print("\n1:Inset ")
           print("2:Delete")
           print("3:Display")
           print("4:Exit")
           c=int(input("Enter your choice:"))
           if(c==1):
               val=int(input("Enter value:"))
               rear,front=cq.enqueue(circularque,rear,front,val,size)
           elif(c==2):
             item,front,rear=cq.dequeue(circularque,rear,front,size)
             print("Remove Element:",item)
           elif(c==3):
              sq.display(circularque)
           elif(c==4):
               break
           else:
               print("Enter valid input")
    elif(choice==3):
         
         while(True):
           print("\n1:Inset Right ")
           print("2:Inset Left ")
           print("3:Delete Right")
           print("4:Delete Left")
           print("5:Display")
           print("6:Exit")
           c=int(input("Enter your choice:"))
           
           if(c==1):
               val=int(input("Enter value:"))
               dq.append_right(doublque,val)
           elif(c==2):
               val=int(input("Enter value:"))
               dq.append_left(doublque,val)
           elif(c==3):
               print("Remove Element",dq.pop_right(doublque))
           elif(c==4):
               print("Remove Element",dq.pop_left(doublque))
           elif(c==5):
               dq.display(doublque)
           elif(c==6):
               break
           else:
               print("Enter valid input")
            

    
     


