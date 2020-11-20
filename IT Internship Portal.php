<?php header( 'Location: /IT Internship Portal.html' ) ;  ?>
<!DOCTYPE html>
<html lang="en">
  <head>

    <meta charset="utf-8">
    <link rel="stylesheet" href="css/mystyle.css">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    
    <link href="https://fonts.googleapis.com/css?family=Work+Sans:300,400,500,600,700" rel="stylesheet">

    <link rel="stylesheet" href="css/open-iconic-bootstrap.min.css">
    <link rel="stylesheet" href="css/animate.css">
    
    <link rel="stylesheet" href="css/owl.carousel.min.css">
    <link rel="stylesheet" href="css/owl.theme.default.min.css">
    <link rel="stylesheet" href="css/magnific-popup.css">

    <link rel="stylesheet" href="css/aos.css">

    <link rel="stylesheet" href="css/ionicons.min.css">

    <link rel="stylesheet" href="css/bootstrap-datepicker.css">
    <link rel="stylesheet" href="css/jquery.timepicker.css">
    <link rel="stylesheet" href="css/flaticon.css">
    <link rel="stylesheet" href="css/icomoon.css">
    <link rel="stylesheet" href="css/style.css">
    <link rel="stylesheet" href="css/typingstyle.scss">
    
    <style type="text/css">
p {text-align: center;}
</style>
  </head>
  <body>
    <nav class="navbar navbar-expand-lg navbar-dark ftco_navbar bg-dark ftco-navbar-light" id="ftco-navbar">
      <div class="container">
        <a class="navbar-brand" href="IT Internship Portal.php">IT Internship Portal</a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#ftco-nav" aria-controls="ftco-nav" aria-expanded="false" aria-label="Toggle navigation">
          <span class="oi oi-menu"></span> Menu
        </button>
        
        <div class="collapse navbar-collapse" id="ftco-nav">
          <ul class="navbar-nav ml-auto">
            <li class="nav-item active"><a href="IT Internship Portal.php" class="nav-link">Home</a></li>
            <li class="nav-item"><a href="about.php" class="nav-link">About</a></li>
            <li class="nav-item"><a href="http://wojciechwydmuch.com/contact.php" class="nav-link">Contact</a></li>
          <li class="nav-item cta"><a href="#1" class="nav-link"><span>Get started</span></a></li>
          </ul>
        </div>
      </div>
    </nav>
    <div class="hero-wrap js-fullheight img" style="background-image: url(images/bg_1.jpg);">
      <div class="overlay"></div>
      <div class="container-fluid px-0">
        <div class="row d-md-flex no-gutters slider-text align-items-center js-fullheight justify-content-center">
          <div class="col-md-8 text-center d-flex align-items-center ftco-animate js-fullheight">
            <div class="text mt-5">
              <span class="subheading">Are you looking for an internship?</span>
              <h1 class="mb-3"><p>IT Internship Portal<p></h1>
              <p>Find a job in IT and gain experience</p>
            
            <a href="#1" class="btn btn-secondary px-4 py-3">Get Started Now</a></li>
            </div>
          </div>
        </div>
      </div>
    </div>
    <section class="ftco-section ftco-partner">
      <div class="container">
        <div class="row">
          <div class="col-sm ftco-animate">
            <a href="#" class="partner"><img src="images/partner-1.png" class="img-fluid" alt="Colorlib Template"></a>
          </div>
          <div class="col-sm ftco-animate">
            <a href="#" class="partner"><img src="images/partner-2.png" class="img-fluid" alt="Colorlib Template"></a>
          </div>
          <div class="col-sm ftco-animate">
            <a href="#" class="partner"><img src="images/partner-3.png" class="img-fluid" alt="Colorlib Template"></a>
          </div>
          <div class="col-sm ftco-animate">
            <a href="#" class="partner"><img src="images/partner-4.png" class="img-fluid" alt="Colorlib Template"></a>
          </div>
          <div class="col-sm ftco-animate">
            <a href="#" class="partner"><img src="images/partner-5.png" class="img-fluid" alt="Colorlib Template"></a>
          </div>
        </div>
      </div>
    </section>
        <section class="ftco-section ftco-counter bg-light img" id="section-counter">
      <div class="container">
        <div class="row justify-content-center">
          <div class="col-md-3 d-flex justify-content-center counter-wrap ftco-animate">
            <div class="block-18 text-center">
              <div class="text">
                <strong class="number" data-number="100">0</strong>
                <span>Internship offers</span>
              </div>
            </div>
          </div>
          <div class="col-md-3 d-flex justify-content-center counter-wrap ftco-animate">
            <div class="block-18 text-center">
              <div class="text">
                <strong class="number" data-number="70">0</strong>
                <span>Companies</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
   
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/material-design-iconic-font/2.2.0/css/material-design-iconic-font.min.css" integrity="sha256-3sPp8BkKUE7QyPSl6VfBByBroQbKxKG7tsusY2mhbVY=" crossorigin="anonymous" />
     <section id="1">
<div class="container">
  <br>
  <br>
   
            <div class="row">

                <div class="col-lg-10 mx-auto">

                    <div class="career-search mb-60">


                    <div class="filter-result">
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
                             $company = $row['company_name']; 
                             $location = $row['location'];
                             $url = $row['url_address'];

                        ?>

                          
                             <div class="job-box d-md-flex align-items-center justify-content-between mb-30">
                                 <div class="job-left my-4 d-md-flex align-items-center flex-wrap">

                                    <div class="img-holder mr-md-4 mb-md-0 mb-4 mx-auto mx-md-0 d-md-none d-lg-flex">
                                     <?php echo $company[0]; ?>
                                    </div>
                                    <div class="job-content">
                                    <div class="text">
                                        <h5 class="text-center text-md-left"><?php echo $title; ?></h5>
                                        <ul class="d-md-flex flex-wrap text-capitalize ff-open-sans">
                                            <li class="mr-md-4">
                                                <i class="zmdi zmdi-home mr-2"> <?php echo $company; ?></i> 
                                            </li>
                                            <li class="mr-md-4">
                                                <i class="zmdi zmdi-pin mr-2"></i> <?php echo $location; ?>
                                            </li>
                                        </ul>
                                    </div>
                                    </div>
                                </div>
                                <div class="job-right my-4 flex-shrink-0">
                                    <a href=<?php echo $url ?> class="btn d-block w-100 d-sm-inline-block btn-light">Aplikuj teraz</a>
                                </div>
                            </div>
                     <?php } ?> 
 
                    <!-- START Pagination -->
                    <nav aria-label="Page navigation">
                        <ul class="pagination pagination-reset justify-content-center">
                            
                            </li>
                           
                            
                        </ul>
                    </nav>
                    <!-- END Pagination -->
                </div>
              
            </div>

        </div>
    
<script src="http://code.jquery.com/jquery-1.10.2.min.js"></script>
<script src="http://netdna.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js"></script>
<script type="text/javascript"></script>

    </section>

            <p><!-- Link back to Colorlib can't be removed. Template is licensed under CC BY 3.0. -->
     Copyright &copy;<script>document.write(new Date().getFullYear());</script> All rights reserved | This template is made with <i class="icon-heart" aria-hidden="true"></i> by <a href="https://colorlib.com" target="_blank">Colorlib</a>
  <!-- Link back to Colorlib can't be removed. Template is licensed under CC BY 3.0. --></p>
   
    
  

  <!-- loader -->
  <div id="ftco-loader" class="show fullscreen"><svg class="circular" width="48px" height="48px"><circle class="path-bg" cx="24" cy="24" r="22" fill="none" stroke-width="4" stroke="#eeeeee"/><circle class="path" cx="24" cy="24" r="22" fill="none" stroke-width="4" stroke-miterlimit="10" stroke="#F96D00"/></svg></div>


  <script src="js/jquery.min.js"></script>
  <script src="js/jquery-migrate-3.0.1.min.js"></script>
  <script src="js/popper.min.js"></script>
  <script src="js/bootstrap.min.js"></script>
  <script src="js/jquery.easing.1.3.js"></script>
  <script src="js/jquery.waypoints.min.js"></script>
  <script src="js/jquery.stellar.min.js"></script>
  <script src="js/owl.carousel.min.js"></script>
  <script src="js/jquery.magnific-popup.min.js"></script>
  <script src="js/aos.js"></script>
  <script src="js/jquery.animateNumber.min.js"></script>
  <script src="js/scrollax.min.js"></script>
  <script src="https://maps.googleapis.com/maps/api/js?key=AIzaSyBVWaKrjvy3MaE7SQ74_uJiULgl1JY0H2s&sensor=false"></script>
  <script src="js/google-map.js"></script>
  <script src="js/main.js"></script>
    
  </body>
</html>