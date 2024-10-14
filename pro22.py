import re

data="""Gujarat Vidyapith was founded by Mahatma Gandhi a@gmail.com on 18th October, 1920. 
        Gujarat Vidyapith is a deemed university since 1963. a.gvp@gmail.com Gujarat Vidyapith is funded by the U. G. C. (University Grants Commission) for higher education programs.
        It was started as Rashtriya Vidyapith 333 123 4567 (National Institute of University Education)abcd@ernef.in and was the wake of the Non-cooperative Movement. Mahatma Gandhi remained its life-long Kulpati (Chancellor). 
        The Institute imparts higher a-b@gujarat education with an integrated system of education teaching from the Nursery to the Doctorate level."""

emp1=r"\w\@\w+\.\w+"

emp2=r"\w\.\w+\@\w+\.\w+"

emp3=r"\w+\@\w+\.\w+"

emp4=r"\w\-\w\@\w+"

pattern=emp1+"|"+emp2+"|"+emp3+"|"+emp4


for i in re.findall(pattern,data):
    print(i)
