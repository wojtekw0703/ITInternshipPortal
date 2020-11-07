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
         echo $row['location'];
      }

    mysqli_close($con);
    ?>  