## UploadData

Little piece of code to upload grades of students

## dropdown
Users can select a faculty, a program and a course from a dropdown.

  These options are shown in options.json

  The update of the dropdown happens in showDropdown.js

## Uploading

We expect the user to upload a csv file (, or ; separated) with two columns:

  studentid and grades

  The studentid must be an integer

  The grades must be an integer between 0 and 20 or # or NA

  This checking happens in upload.php

  There are some sample files in the folder samples to illustrate

## Saving

We save the grades in ../uploads

## Converting

When the grades are uploaded, we convert all of them in a json file

  We do this in the parseCSV.py file

  run python parseCSV.Py

## License
