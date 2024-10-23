import csv
import itertools

tutorial_groups = {}

# Read the CSV file
def read_csvfile(filename):
    allstudents = []
    with open(filename, 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            allstudents.append({
                'Tutorial Group': row['Tutorial Group'],
                'Student ID': row['Student ID'],
                'School': row['School'],
                'Name': row['Name'],
                'Gender': row['Gender'],
                'CGPA': float(row['CGPA'])
            })
    return allstudents
    

def groupbasedontutgrp(students): # Group students by tutorial group 
    list_of_sch = []
    for i in students:
        if i["School"] not in list_of_sch:
            list_of_sch.append(i["School"])
    print(len(list_of_sch)) #18 schools
    

    for student in students: #For each student in student, the tutgroup will append the student based on said tutorial group
        tutgroup = student['Tutorial Group']
        if tutgroup not in tutorial_groups: #if tutgroup is not stated, it will create a new one
            tutorial_groups[tutgroup] = []
        tutorial_groups[tutgroup].append(student) 
        #e.g student {'Tutorial Group': 'G-10', 'Student ID': '3329', 
        #'School': 'MAE', 'Name': 'Adrian Castillo', 'Gender': 'Male', 'CGPA': 4.07} student is a dict in a list
    #print(tutorial_groups["G-10"]) #to pull out one tutorial group, access it like dictionary key

    # Print the number of students and tutorial groups
    #print(f"Total number of students: {len(students)}")
    #print(f"Total number of tutorial groups: {len(tutorial_groups)}")

    return tutorial_groups


def analyze_and_sort_by_gender_cgpa(students):
    
    males = []
    females = []
    #Sort students based on gender and split them into 2 list: males and females
    for s in students:
        if s['Gender'] == 'Male':
            males.append(s)
        else:
            females.append(s)
    
    #To assess between male to female ratio for all students in each tutorial group
    male_ratio = len(males) / len(students) 
    female_ratio = len(females) / len(students)


    
    # Sort males and females by CGPA from min to max, I use stackoverflow for this, may need to declare
    males = sorted(males, key=lambda student: student['CGPA'])
    females = sorted(females, key=lambda student: student['CGPA'])

    #males.sort(key=lambda student: student['CGPA']) #another way to write to sort

    #Bubble sort to ensure change in school
    for group in range(len(males)):
        for i in range(0, len(males)-group-1):
            if males[i]['School'] == males[i+1]['School']:
                males[i], males[i+1] = males[i+1],males[i]
            

    #for i in males:
        #if i["Tutorial Group"] == "G-10":
            #print(i)
    
    
    #print(male_ratio, female_ratio)
    
    return males, females, male_ratio, female_ratio
    

def main():
    # Read the CSV file, can shift it to main later
    students = read_csvfile('records.csv')
    tutorial_groups = groupbasedontutgrp(students)
    # Analyze and sort students by gender and CGPA within each tutorial group
    for group in tutorial_groups:
        male, female, female_ratio, male_ratio = analyze_and_sort_by_gender_cgpa(tutorial_groups[group])

main()