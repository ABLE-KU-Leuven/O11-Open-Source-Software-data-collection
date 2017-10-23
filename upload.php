<?php
    /*
    check if consist of 2 values
    check if studentId is integer
    check if grades is intiger in range 0-20 or NA or #

    */
    function checkValidData($data) {

        if (count($data) != 2){
            return false;
        }
        if (!is_numeric($data[0])){
            return false;
        }
        if (!is_numeric($data[1])){
            if ($data[1] == "NA" || $data[1] == "#"){
                return true;
            }
            else{
                return false;
            }
        }
        $studentId = (int)$data[0];
        $grades = (int)$data[1];
        if ($grades < 0 || $grades > 20){
            return false;
        }
        else{
            return true;
        }
    }
    $faculty = $_POST['faculties'];
    $program = $_POST['programs'];
    $course = $_POST['courses'];
    $target_dir = "../uploads/";

    $fname = $faculty.$program.$course.'.csv';
    $target_file = $target_dir . $fname;
    $success = true;
    if ($_FILES['csv']['size'] > 0) {
            //get the csv file
            $file = $_FILES['csv']['tmp_name'];
            //replace ; by , if needed
            $content=file_get_contents($file);
            $content_chunks=explode(';', $content);
            $content=implode(',', $content_chunks);
            file_put_contents($file, $content);
            //
            $handleUploaded = fopen($file,"r");
            $output_CSV[0] = array('faculty','proram', 'course', 'studentid', 'grades');
            $nb = 1;
            while ( $data = fgetcsv($handleUploaded,1000,",","'")){
                if (checkValidData($data)) {
                    $output_CSV[$nb] = array($faculty, $program, $course, $data[0], $data[1]);
                    $nb += 1;
                }
                else{
                    $success = false;
                    $message = "We think something is wrong on line $nb";
                    echo "<script type='text/javascript'>
                    alert('$message');
                    window.location.href='https://learninganalytics.set.kuleuven.be/lissa1718-upload/';
                    </script>";

                }
            }
            fclose($handleUploaded);
    }
    if ($success){
        $handleWrite = fopen($target_file, "w");
        foreach ($output_CSV as $line) {
            fputcsv($handleWrite, $line, ',');
        }
        $nbStudents = $nb -1;
        $printfname = basename($_FILES["csv"]["name"]);
        echo "You uploaded: $printfname <br/>" ;
        echo "This file contained: $nbStudents students";
        fclose($handleWrite);

    }


?>
