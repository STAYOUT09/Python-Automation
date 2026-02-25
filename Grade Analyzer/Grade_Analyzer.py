def grade(marks): 
    if marks >= 90.0: 
        return 'A' 
    elif marks >= 80.0: 
        return 'B' 
    elif marks >= 70.0: 
        return 'C' 
    elif marks >= 60.0: 
        return 'D' 
    else: 
        return 'F' 

def analyze_grades(marks): 
    Total = sum(marks) 
    Average = Total / len(marks) 
    Highest = max(marks) 
    Lowest = min(marks) 
    return Total, Average, Highest, Lowest 

marks=[]
students = int(input("Enter the number of students: ")) 
for i in range(students): 
    mark = float(input(f"Enter marks for student {i+1}: ")) 
    marks.append(mark) 

Total, Average, Highest, Lowest = analyze_grades(marks) 

print("\nResult Summary:") 
print(f"Total Marks: {Total}") 
print(f"Average Marks: {Average}") 
print(f"Highest Marks: {Highest}") 
print(f"Lowest Marks: {Lowest}") 

print("\nGrades:") 
for i in range(students): 
    print(f"Student {i+1}: Marks = {marks[i]}, Grade = {grade(marks[i])}")