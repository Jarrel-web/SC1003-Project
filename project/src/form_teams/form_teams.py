from form_teams.find_gender_constraint import gender_constraint
from form_teams.select_student_functions import *
def form_teams(students, team_size): 
    teams = []
    #Number of students from the same school constraint
    max_school_ratio=0.5 
    target_teams = int(len(students)/team_size)
    try:
        while students and len(teams) <target_teams: 
            target_male,target_female = gender_constraint(students, team_size)
            
            team = []
            school_count = {}
            while len(team) < team_size:
                if len(team)%2 == 0:
                    selected_student,students,target_male,target_female = select_student(students,target_male,
                                                    target_female,school_count,
                                                    max_school_ratio*team_size,True)
                    if selected_student: 
                        team.append(selected_student)
                        school_count = update_school_count(selected_student, school_count)
                    else:
                        middle_index = len(students)//2 
                        team.append(students.pop(middle_index))
                else:
                    selected_student,students,target_male,target_female = select_student(students,target_male,
                                                    target_female,school_count,
                                                    max_school_ratio*team_size,False)
                    if selected_student:
                        team.append(selected_student)
                        school_count = update_school_count(selected_student, school_count)
                    else:
                        middle_index = len(students)//2 
                        team.append(students.pop(middle_index))
            teams.append(team) 

    except IndexError as e:
        raise RuntimeError(f"An error occurred while processing students: {e}")
    return teams