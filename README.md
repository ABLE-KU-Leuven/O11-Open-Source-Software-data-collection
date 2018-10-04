## Description
Tool to upload grades of students for use in LISSA (https://github.com/ABLE-KU-Leuven/LISSA-Dashboard) and CSE tool (https://github.com/ABLE-KU-Leuven/CSETool) 

## Pointers to publications
### Case study report
http://www.ableproject.eu/project/reports-three-institutional-case-studies/

### Data collection and utilization
http://www.ableproject.eu/project/report-methods-and-tools-to-collect-and-utilise-data/

### Scientific publications 
* Charleer, S., Moere, A. V., Klerkx, J., Verbert, K., & De Laet, T. (2017). Learning analytics dashboards to support adviser-student dialogue. IEEE Transactions on Learning Technologies. Volume 11, issue 3, https://ieeexplore.ieee.org/abstract/document/7959628/ 
* Millecamp, M., Gutiérrez, F., Charleer, S., Verbert, K., & De Laet, T. (2018, March). A qualitative evaluation of a learning dashboard to support advisor-student dialogues. In Proceedings of the 8th International Conference on Learning Analytics and Knowledge (pp. 56-60). https://dl.acm.org/citation.cfm?id=3170417 

## Howto
### UploadData

Little piece of code to upload grades of students

To test it local: run php -S localhost:8000

### dropdown
Users can select a faculty, a program and a course from a dropdown.

  These options are shown in options.json

  The update of the dropdown happens in showDropdown.js

### Uploading

We expect the user to upload a csv file (, or ; separated) with two columns:

  studentid and grades

  The studentid must be an integer

  The grades must be an integer between 0 and 20 or # or NA

  This checking happens in upload.php

  There are some sample files in the folder samples to illustrate

### Saving

We save the grades in ../uploads

### Converting

When the grades are uploaded, we convert all of them in a json file

  We do this in the parseCSV.py file

  run python parseCSV.Py

### License
