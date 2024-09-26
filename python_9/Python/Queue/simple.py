
   
def enqueue(queue,item):
  
    queue.append(item)

def dequeue(queue):

    if queue:
        return queue.pop(0)
    else: 
        print("Que is empty")
        return None

def display(queue):
     for i in queue:
          print(i,end=" ")
     



