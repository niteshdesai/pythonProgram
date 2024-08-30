class AcademicRecord:
    def __init__(self):
        self.courses = {}  # Dictionary to store course data

    def add_course(self, course_name, credits, points):
        """Add a new course with total credits and earned points."""
        self.courses[course_name] = {'credits': credits, 'points': points}
        print(f"Course '{course_name}' added with {credits} credits and {points} points.")

    def drop_course(self, course_name):
        """Drop a course."""
        if course_name in self.courses:
            del self.courses[course_name]
            print(f"Course '{course_name}' has been dropped.")
        else:
            print(f"Course '{course_name}' not found.")

    def print_record(self):
        """Print the whole academic record."""
        if not self.courses:
            print("No courses recorded.")
            return
        
        print("Academic Record:")
        for course_name, data in self.courses.items():
            credits = data['credits']
            points = data['points']
            print(f"Course: {course_name}, Credits: {credits}, Points: {points}")

    def calculate_cgpa(self):
        """Calculate and return the current CGPA."""
        total_credits = sum(data['credits'] for data in self.courses.values())
        total_points = sum(data['credits'] * data['points'] for data in self.courses.values())
        
        if total_credits == 0:
            print("No courses recorded. CGPA cannot be calculated.")
            return 0
        
        cgpa = total_points / total_credits
        return cgpa

# Example usage:
record = AcademicRecord()

# Add courses
record.add_course("Mathematics", 4, 3.5)
record.add_course("Physics", 3, 3.0)
record.add_course("Chemistry", 3, 3.8)

# Drop a course
record.drop_course("Physics")

# Print the academic record
record.print_record()

# Calculate CGPA
cgpa = record.calculate_cgpa()
print(f"Current CGPA: {cgpa:.2f}")
