import re

data="""Gujarat Vidyapith was founded by Mahatma Gandhi 12345 67890 on 18th October, 1920. 
        Gujarat Vidyapith is a deemed university since 1963.11 98765 4321 Gujarat Vidyapith is funded by the U. G. C. (University Grants Commission) for higher education programs.
        It was started as Rashtriya Vidyapith 333 123 4567 (National Institute of University Education)343-321-672 and was the wake of the Non-cooperative Movement. Mahatma Gandhi remained its life-long Kulpati (Chancellor). 
        The Institute imparts higher (92) 7321-4348 education with an integrated system of education teaching from the Nursery to the Doctorate level."""


ptr1=r"\d{5}\s\d{5}"

ptr2=r"\d{2}\s\d{5}\s\d{4}"

ptr3=r"\d{3}\D\d{3}\D\d{3}"

ptr4=r"\(\d{2}\)\s\d{4}\D\d{4}"



pattern=ptr1+"|"+ptr2+"|"+ptr3+"|"+ptr4

matchdata=re.findall(pattern,data)

for i in matchdata:
    print(i)
