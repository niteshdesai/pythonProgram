
def insert(que,r,f):
	
	if(r==len(que) and f==0 or r==f-1):

		print("que is full\n")

	else:

		print("Enter Element:")
		val=int(input())

		if(r==-1 and f==-1):
			f=0
			r=0
			que.append(val)

		elif(r==max-1 and f!=0):
			r=0
			que.append(val)
		else:
			r+=1
			que.append(val)
		

	



def removesq(que,r,f):
	    if(f==-1 and r==-1):
		     print("\nque is empty:")
        elif(f==r):
    #   print(que[f])
	# 	 que[f]=0
	# 	 f=-1
	# 	 r=-1
	
# 	 else if(*f==max-1&&*r<*f)
# 	 {
# 		 printf("\n%d",que[*f]);
# 		 que[*f]=0;
# 	     *f=0;
# 	 }
# 	 else
# 	 {
		 
# 		 printf("\n%d\n",que[*f]);
# 		 que[*f]=0;
# 		 *f=*f+1;
# 	 }
# }

def display(que):

	 for i in que:
		 print(i)
	
# int simpleFind(int *r,int *f,int serchEl)
# {
#   int i=0,t=0;

#      for(i=0;i<=max;i++)
#      {
#        if(que[i]==serchEl)
#        {
#         t=i;
#         break;
#        }
#      } 



#   if(i>max)
#   {
#     return -1;
#   }
#   return t;
# }
# void modify(int *r,int *f)
# {
#   int ind,ne,pe;
#    printf("\nEnter old value:");
#    scanf("%d",&pe);
#    printf("\nEnter new value:");
#    scanf("%d",&ne);
#    ind=simpleFind(r,f,pe);
#    if(ind!=-1)
#    {
#      que[ind]=ne;
#      printf("Change value %d  to %d",pe,ne);
#    }
#    else
#    {
#      printf("\nElement is not present in array");
#    }
   


que=[] 
f=-1
r=-1
while(True):

		print("\n1:insert:")
		print("\n2:remove:")
		print("\n3:modify:")
		print("\n4:exit:")
		
		print("\nEnter your choice:")
		c=int(input())
		if(c==1):
			insert(que,f,r)
			display(que)
	

		# case 2:removesq(r,f);
		# 	   display();
		# 	   break;
	 	# case 3:modify(r,f);
		# 	   display();
		# 	   break;
		# case 4:exit(0);

# 		}
# 	}
	
# }