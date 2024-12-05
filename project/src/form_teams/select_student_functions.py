#5 Function to select a student without violating the school ratio   
def select_student(students,target_male,target_female,school_count,max_school_ratio,remove_from_front):
    female_student = False
    male_student = False
    valid_school_constraint = False
    selected_student = None
    if remove_from_front:
        # Iterate from the front of the list
        for i in range(len(students)):
            school = students[i]['School']
            gender = students[i]['Gender']
            if school_count.get(school, 0)+1 < max_school_ratio:
                valid_school_constraint = True
            if gender == 'Male'and target_male != 0:
                target_male -= 1
                male_student = True
            elif gender == 'Female' and target_female != 0:
                target_female -=1
                female_student = True
            if (female_student or male_student) and valid_school_constraint:
                selected_student = students.pop(i)
                return selected_student,students,target_male,target_female
    else:
        # Iterate from the back of the list
        for i in range(len(students) - 1, -1, -1):
            school = students[i]['School']
            gender = students[i]['Gender']
            if school_count.get(school, 0)+1 < max_school_ratio:
                valid_school_constraint = True
            if gender == 'Male' and target_male != 0:
                target_male -= 1
                male_student = True
            elif gender == 'Female' and target_female != 0:
                target_female -=1
                female_student = True
            if (female_student or male_student) and valid_school_constraint:
                selected_student = students.pop(i)
                return selected_student,students,target_male,target_female
    return None,students,target_male,target_female
    

#4 Function to update school counts
def update_school_count(student,school_count):
   
    school = student['School']
    if school in school_count:
        school_count[school] += 1
    else:
        school_count[school] = 1
    return school_count