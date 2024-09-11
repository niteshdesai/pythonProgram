import acedemicoperation as operation
operation.add_course("Math", 4, 3.5)
operation.add_course("Science", 3, 4.0)
operation.print_record()
print("\nCurrent CGPA:  ",operation.calculate_cgpa())
operation.drop_course("Math")
operation.print_record()
print("Current CGPA: {}".format(operation.calculate_cgpa()))
