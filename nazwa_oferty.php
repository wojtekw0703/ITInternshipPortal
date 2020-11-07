<?php
    $con=mysqli_connect("localhost","root@","","internship_database");
    // Check connection
    if (mysqli_connect_errno())
      {
      echo "Failed to connect to MySQL: " . mysqli_connect_error();
      }

    $result = mysqli_query($con,"SELECT * FROM internships");

    while($row = mysqli_fetch_array($result))
      {
       $title= $row['job_title'];
        $company = $row['company_name']; //these are the fields that you have stored in your database table employee
        $location = $row['location'];
      }

    mysqli_close($con);
    ?>  