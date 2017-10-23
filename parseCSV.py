import os
import csv
import json

def getFaculty(filename):
    ABA =  filename.split('ABA')
    SMA =  filename.split('SMA')
    if len(ABA) > 1:
        return ABA[0]
    elif len(SMA) > 1:
        return SMA[0]
    else:
        print 'error'
        return filename


def getProgram(programcourse):
    """
    find program in given string consisting of program and course
    Alle vakken starten met Ijkingstoets, Positioneringstest, Voorkennistest of TTT
    """
    ttt = programcourse.split('TTT')
    Ijk = programcourse.split('Ijk')
    Pos = programcourse.split('Pos')
    Voo = programcourse.split('Voor')

    if len(ttt) > 1:
        return ttt[0]
    elif len(Ijk) > 1:
        return Ijk[0]
    elif len(Pos) > 1:
        return Pos[0]
    elif len(Voo) > 1:
        return Voo[0]
    else:
        return ''

def getRemaining(filename, string):
    """
    Given filename consisting of faculty-program-course
    cut the faculty of it
    return programcourse
    """
    return filename.replace(string, '')

def getSemester(course):
    if course.startswith('TTT'):
        return 'B'
    else:
        return 'A'

def getCourse(courseextension):
    return courseextension.split('.')[0]

def writeGradesCSV(filename, writepath, course):
    gradesToCSV = []
    with open(filename, 'rb') as csvfile:
        next(csvfile)
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
             studentid = row[0]
             score = row[1]
             gradesToCSV.append([studentid, course, score, 'J', '2017-2018', score, '#'])
    if not os.path.isfile(writepath):
        gradesToCSV.insert(0,['studentid','courseid', 'finalscore', 'generatiestudent', 'year', 'grade_try1', 'grade_try2'])

    with open(writepath, 'a') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        for row in gradesToCSV:
            writer.writerow(row)

def writeToJSON(csvfile):
    filename, file_extension = os.path.splitext(csvfile)
    csvfile = open('output/' + csvfile, 'r')
    jsonfile = open('JSON/' + filename + ".json", 'w')

    fieldnames = csvfile.readline().rstrip('\r\n').split(',')
    print fieldnames
    reader = csv.DictReader( csvfile, fieldnames)
    for row in reader:
        json.dump(row, jsonfile)
        jsonfile.write('\n')

directory = '../upload/'
coursesToCSV = [['faculty', 'program','courseid', 'credits', 'coursename', 'semester', 'phase', 'block']]
files = []
for filename in os.listdir(directory):
    if filename.endswith(".csv"):
        files.append(filename)
        faculty = getFaculty(filename)
        programcourse = getRemaining(filename, faculty)
        program = getProgram(programcourse)
        courseextension = getRemaining(programcourse, program)
        course = getCourse(courseextension)
        semester = getSemester(course)
        coursesToCSV.append([faculty, program, course, 0, course, semester, 1, '#' ])
        filepath = directory + filename
        writepath = 'output/'+ faculty + '_'+ program + '_' + "grades.csv"
        writeGradesCSV(filepath, writepath, course)
    else:
        continue
with open('output/courses.csv', 'wb') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    for row in coursesToCSV:
        writer.writerow(row)

for filename in os.listdir('output/'):
    writeToJSON(filename)
