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

    $target_dir = "uploads/";
    $prefix = $_POST['faculties'];
    echo $prefix;
    $fname = basename($_FILES["csv"]["name"]);
    $target_file = $target_dir . basename($_FILES["csv"]["name"]);
    //$_FILES[csv] gives the uploaded file as array with
    // Name, type, tmp_name, error and size 
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
                    $message = "wrong line on line $nb";
                    echo "<script type='text/javascript'>alert('$message');</script>";
                    $success = false;
                    break;
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
        echo "You uploaded: $fname <br/>" ;
        echo "This file contained: $nbStudents students";
        fclose($handleWrite);
        
    }
    

?>