def sort_by_tutorialgrp(students):
    tutorial_groups = {}
    for student in students: #For each student in student, the tutgroup will append the student based on said tutorial group
        tutgroup = student['Tutorial Group']
        if tutgroup not in tutorial_groups: #if tutgroup is not stated, it will create a new one
            tutorial_groups[tutgroup] = []
        tutorial_groups[tutgroup].append(student) 
        #e.g student {'Tutorial Group': 'G-10', 'Student ID': '3329', 
        #'School': 'MAE', 'Name': 'Adrian Castillo', 'Gender': 'Male', 'CGPA': 4.07} student is a dict in a list
    for group, students in tutorial_groups.items():
        students.sort(key=lambda student: student['CGPA'])
    return tutorial_groups