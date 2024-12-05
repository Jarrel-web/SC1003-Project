import csv

def read_csvfile(filepath):
    allstudents = []
    try:
        with open(filepath, 'r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                try:
                    allstudents.append({
                    'Tutorial Group': row.get('Tutorial Group', 'Unknown'),
                    'Student ID': row.get('Student ID', 'Unknown'),
                    'School': row.get('School', 'Unknown'),
                    'Name': row.get('Name', 'Unknown'),
                    'Gender': row.get('Gender', 'Unknown'),
                    'CGPA': float(row.get('CGPA',0.0))
                })
                except ValueError:
                    print(f"Invalid CGPA value in row {row}")
                    continue        
    except(FileNotFoundError, PermissionError) as e:
         print(f"An error occurred: {e}")
    except Exception as e:  
         print(f"An error occurred: {e}")
    return allstudents
    
def write_csv(all_teams):
    with open('assign_team_records.csv','w') as file:
        file.write('Tutorial Group,Student ID,School,Name,Gender,CGPA,Team Assigned\n')
        for student in all_teams:
            tut_grp=student.get('Tutorial Group')
            student_id=student.get('Student ID')
            school=student.get('School')
            name=student.get('Name')
            gender=student.get('Gender')
            cgpa=str(student.get('CGPA'))
            team_assigned=student.get('Team Assigned')
            file.write(tut_grp+','+student_id+','+school+','+name+','+gender+','+cgpa+','+team_assigned+'\n')