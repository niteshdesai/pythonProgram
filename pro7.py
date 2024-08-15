suit_card=("spade","heart", "diamond","club")
s=input("Enter Any Suit with Card : ").lower()

while(1):
 if(len(s.split())!=2):
     s=input("Enter Any Suit with Card : ").lower()
 else:
   break

while(1):
  suit,card=s.split()
  if(suit in suit_card):
    break
  else:
         s=input("Enter Any Suit with Card : ").lower()
         if(len(s.split())!=2):
              s=input("Enter Any Suit with Card : ").lower()
        

print()
if((suit=='diamond' and card=='king')or (suit=='spade'or card=='ace')or(suit=='heart'and card=='queen')or (suit=='clube'and card=='joker')):
  print("Card is Lucky")
else:
  print("Please,try next time")