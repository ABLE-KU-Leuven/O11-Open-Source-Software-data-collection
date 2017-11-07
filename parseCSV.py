import os
import csv
import json

def getFaculty(filename):
    """
    Find faculty in given filename
    filename is built as directory/facultyprogramcourse.csv
    All programs starts with ABA or SMA
    """
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
    """
    Get the semester based on the name of the course
    """
    if course.startswith('TTT'):
        return -1
    else:
        return -2

def getCourse(courseextension):
    """
    Given course.extension
    return course
    """
    return courseextension.split('.')[0]

def writeGradesCSV(filepath, filename, writepath):
    """
    filename: path of input file (only studentid and grade)
    writepath: path of output file of complete csv file (multiple fields)
    """
    # get all field values based on filename
    faculty = getFaculty(filename)
    programcourse = getRemaining(filename, faculty)
    program = getProgram(programcourse)
    courseextension = getRemaining(programcourse, program)
    course = getCourse(courseextension)

    gradesToCSV = []
    with open(filepath, 'rb') as csvfile:
        next(csvfile)
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
             studentid = row[0]
             score = row[1]
             gradesToCSV.append([faculty, program, studentid, course, score, 'J', '2016-2017', score, '#'])
    # If the file not exist, write the fields to it
    if not os.path.isfile(writepath):
        gradesToCSV.insert(0,['faculty', 'program','studentid','courseid', 'finalscore', 'generatiestudent', 'year', 'grade_try1', 'grade_try2'])

    with open(writepath, 'a') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        for row in gradesToCSV:
            writer.writerow(row)

def writeCoursesCSV(filepath, filename, writepath):
    """
    filename: path of input file (only studentid and grade)
    writepath: path of output file of complete csv file (multiple fields)
    """
    # get all field values based on filename
    faculty = getFaculty(filename)
    programcourse = getRemaining(filename, faculty)
    program = getProgram(programcourse)
    courseextension = getRemaining(programcourse, program)
    course = getCourse(courseextension)
    semester = getSemester(course)

    coursesToCSV = []

    coursesToCSV.append([faculty, program, course, 0, course, semester, 1, '#' ])
    # If the file not exist, write the fields to it
    if not os.path.isfile(writepath):
        coursesToCSV.insert(0,['faculty', 'program','courseid', 'credits', 'coursename', 'semester', 'phase', 'block'])

    with open(writepath, 'a') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        for row in coursesToCSV:
            writer.writerow(row)


def writeToJSON(csvfile):
    filename, file_extension = os.path.splitext(csvfile)
    csvfile = open('output/' + csvfile, 'r')
    jsonfile = open('JSON/' + filename + ".json", 'w')

    fieldnames = csvfile.readline().rstrip('\r\n').split(',')
    reader = csv.DictReader( csvfile, fieldnames)
    for row in reader:
        row = castRow(row)
        json.dump(row, jsonfile)
        jsonfile.write('\n')

def castRow(row):
    """
    Cast the values in inkeys to integers
    """
    newRow = {}
    intkeys = ['studentid', 'finalscore', 'grade_try1', 'grade_try2', 'credits', 'semester']
    for key,value in row.iteritems():
        if key in intkeys:
            try:
                newRow[key] = int(value)
            except:
                newRow[key] = value
                pass
        else:
            newRow[key] = value
    return newRow

def main(directory):
    """
    Parse all (csv)files located in directory to json
    First we make csv files of it and store it in /output
    Then we convert csv files to json and store it in /JSON
    """

    # array where we save
    files = []
    for filename in os.listdir(directory):
        if filename.endswith(".csv"):
            files.append(filename)
            filepath = directory + filename
            coursespath = 'output/courses.csv'
            gradespath = 'output/grades.csv'
            writeGradesCSV(filepath, filename,  gradespath)
            writeCoursesCSV(filepath, filename, coursespath)
        else:
            continue

    for filename in os.listdir('output/'):
        writeToJSON(filename)

directory = '../upload/'
main(directory)
