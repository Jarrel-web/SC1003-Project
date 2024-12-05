def gender_constraint(students,team_size):
    males = 0
    females = 0
    for student in students:
        
        if student.get('Gender') == 'Male':
             males += 1
        else:
            females += 1
    total_students = males+females
    male_ratio = males/total_students
    target_males = min(round(team_size * male_ratio), (team_size // 2 + team_size % 2))  
    target_females = team_size - target_males

    return target_males,target_females