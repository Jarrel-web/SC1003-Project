import csv
student_list =[]
tutGrps_list = []
def populateTutGrpsDict(tutorialGrpsDict, studentList):
    index = 0
    #Gets all the keys in the dict and typecast as a list
    tutorialGrpsDictKeys = list(tutorialGrpsDict.keys())
    for student in studentList:
        # Works in the premise that the students are sorted by tutorial groups already
        if(student.get('tutorialGrp') == tutorialGrpsDictKeys[index]):
            tutorialGrpsDict[tutorialGrpsDictKeys[index]].append(student)
        else:
            index += 1
            tutorialGrpsDict[tutorialGrpsDictKeys[index]].append(student)

with open('data/records.csv',mode='r') as file:
    studentRecordFile = csv.reader(file)
    next(studentRecordFile,None) #skip the header#
    for lines in studentRecordFile:
        #Shows the format of each row in the csv
        print(lines)
        #Gets all the tutorial groups into a list, see line 30
        if(lines[0] not in tutGrps_list):
            tutGrps_list.append(lines[0])
        studentInfo = {
            'tutorialGrp':lines[0],
            'id':lines[1],
            'school':lines[2],
            'name':lines[3],
            'gender':lines[4],
            'gpa':lines[5],
        }
        student_list.append(studentInfo)
print(tutGrps_list)
#creates a dict with a key:value pair where the key is the tutorial group and the value is a list 
tutorialGrps_dict = { grp:[] for grp in tutGrps_list}
populateTutGrpsDict(tutorialGrps_dict,student_list)
#validate by checking if the students are actually from the group
print(tutorialGrps_dict.get('G-99'))



        
        
