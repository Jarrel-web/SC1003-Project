from file_op.file_op import *
from form_teams.sort_group import *
from form_teams.form_teams import *
def main():
    team_size = int(input("Please input team size (4-10): "))
    while team_size<4 or team_size>10:
         print("You have entered a invalid team size")
         team_size = int(input("Please input team size (4-10): "))
    all_teams = []
    file_path = "records.csv"
    students = read_csvfile(file_path)
    tutorial_groups = sort_by_tutorialgrp(students)
    for tutorial_group in tutorial_groups.values():
        teams = form_teams(tutorial_group,team_size)
        for i, team in enumerate(teams, 1):
            for student in team:
                group = student['Tutorial Group']
                student['Team Assigned'] = f"{group}_Team{i}"
            all_teams.extend(team)
    write_csv(all_teams)
if __name__ == '__main__':
    main()  