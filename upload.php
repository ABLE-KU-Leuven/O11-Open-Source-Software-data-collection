<?php
    /*
    check if consist of 2 values
    check if two integers
    check if grades in range 0-20

    */
    function checkValidData($data) {
        
        if (count($data) != 2){
            return false;
        }
        if (!is_numeric($data[0])||!is_numeric($data[1])){
            echo 'I found a string instead of an integer <br/>';
            return false;
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
    $target_dir = "uploads/";
    
    $fname = $faculty.$program.$course.basename($_FILES["csv"]["name"]);
    $target_file = $target_dir . $fname;
    $success = true;
    if ($_FILES['csv']['size'] > 0) {        
            //get the csv file 
            $file = $_FILES['csv']['tmp_name']; 
            $handleUploaded = fopen($file,"r"); 
            $output_CSV[0] = array('studentid', 'grades');
            $nb = 1;
            while ( $data = fgetcsv($handleUploaded,1000,",","'")){
                if (checkValidData($data)) { 
                    $output_CSV[$nb] = array($data[0], $data[1]);
                    $nb += 1;
                } 
                else{
                    $message = "We think something is wrong on line $nb";
                    echo "<script type='text/javascript'>
                    alert('$message');
                    window.location.href='http://www.example.com/';
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
    else{
        header("Location: http://www.example.com/");
    }
    

?>