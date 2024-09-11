import acedemicoperation as operation
choice=0
while True:
    print("1:Add course:")
    print("2:calculate_cgpae:")
    print("3:Drope course")
    print("4:Display Courses")
    print("5:Exit")
    print("Enter your choice")
    choice=int(input())

    if choice==1:
        print("Enter course name") 
        name=input()
        print("Enter credit:")
        credits=float(input())
        print("Enter earned_points")
        earned_points=float(input())
        operation.add_course(name, credits, earned_points)
    elif choice==2:
        print("\nCurrent CGPA:  ",operation.calculate_cgpa())
    elif choice==3:
        print("Enter course name")
        delname=input()
        operation.drop_course(delname)
    elif choice==4:
        operation.print_record()
    elif choice==5:
        break
    else:
        print("Enter valid Choice:")

