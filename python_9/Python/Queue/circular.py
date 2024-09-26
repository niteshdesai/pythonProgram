
def circular_queue(queue,size):
    queue = [None] * size
    return queue
    
def enqueue(queue,rear,front,item,size):
        # if (rear + 1) % size == front:
        if( ((rear==size and front==0 )or rear==front)):
            print("Queue is Full")  
            return rear,front
      
        if(rear==size and front>0):
             rear=0
        if(rear==0 and front==-1):
          front=0
        queue[rear] = item
        rear = rear+1
        return rear,front
def dequeue(queue,rear,front,size):
        if front == -1:
            
            return None,front,rear
        
        item = queue[front]
        queue[front]=0
        if(front==size-1 and rear>0):
           front=0
        elif((front==rear-1) or (front==size-1 and rear==0)):
          front=-1
          rear=0
        else:
             front = front + 1
        return item,front,rear
def display(queue):
     for i in queue:
          print(i,end=" ")


