
def append_right(dq,item):
        
        dq.append(item)

def append_left(dq,item):
        
        dq.insert(0, item)

def pop_right(dq):
       
        if dq:
            return dq.pop()
        return None  

def pop_left(dq):
       
        if dq:
            return dq.pop(0)
        return None  
def display(dq):
       for i in dq:
              print(i,end=" ")

    
