<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <link rel="stylesheet" type="text/css" href="css/bootstrap.css">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Class Notifier</title>
  </head>
  <body>
    <center><h1>UBCO Class Notifier</h1></center>
    <center><h2 style="padding-top: 25px;" class="goAway">Pick a course name</h2></center>
    <center><h2 style="display:none;" id="end_dis" class="later_vis">Type in the details for the course you want to track</h2></center>
    <?php
    $conn = new mysqli("localhost","root","","Hackathon");

    if($conn->connect_error){
      die("Connection failed: ".$conn->connect_error);
    }

    $sql="SELECT * FROM Course_Names";
    $res = $conn->query($sql);
    $result = "<div class=\"container\" id=\"dissapear\">
                <div style=\"height:500px;\" class=\"row\">
                  <div style=\"height:100%;\" class=\"col-sm-4 goAway\"><br class=\"goAway\"><br class=\"goAway\"><p class=\"goAway\">A</p>";
    $counter = 0;
    $letter = "A";
    while($row = $res->fetch_assoc()){
      $letters = str_split($row["Course_Name"]);
      $letter1 = $letters[0];
      if ($letter1 != $letter){
        $result .= "<br class=\"goAway\"><br class=\"goAway\"><p class=\"goAway\">";
        $result .= $letter1;
        $result .= "</p>";
      }
      $letter = $letter1;
      $result .= "<form id=\"frm1\"><input type=\"button\" id=\"course\" onClick=\"showAndSave(this.value)\" name=\"course\" value=\"";
      $result .= ($row["Course_Name"]."\" ");
      $result .= "style=\"margin:5px;\" class=\"btn btn-info goAway\">";
      $counter ++;
      if($counter==30){
        $result .= "</div><center><input type=\"number\" placeholder=\"Course Number\" class=\"later_vis\" style=\"display:none; margin-top:25px;\" id = \"number\" name=\"number\" value=\"\"></center>
        <input type=\"number\" placeholder=\"Section Number\" class=\"later_vis\" style=\"display:none;\" id=\"section\" name=\"section\" value=\"\">
        <input type=\"email\" placeholder=\"example@gmail.com\" class=\"later_vis\" style=\"display:none;\" id = \"email\"name=\"email\" value=\"\">
        <input type=\"button\" class=\"btn btn-success later_vis\" style=\"display:none;\" onClick=\"submitter()\" id=\"later_vis\"  name=\"\" value=\"Submit\"></center>
        <div class=\"col-sm-4\">";
      }
      if($counter == 49){
        $result .= "</div>
        <div class=\"col-sm-4\"> ";
      }
    }
    $result .= "</div>
  </div></form>
</div>

<center><h2 style=\"display:none;\" id=\"end_appear\">Click the link below and send the email to track a course</h2></center><br id=\"end_appear3\">
<center><a href=\"\" id=\"end_link\"><h2 style=\"display:none;\" id=\"end_appear2\">Click here</h2></a></center>

";
    echo $result;



     ?>
     <script type="text/javascript">
        var course = "";
        function showAndSave(val){
          var x = document.getElementsByClassName("goAway");
          var i;
          for (i = 0; i < x.length; i++) {
            x[i].style.display = "none";
          }
          var y = document.getElementsByClassName("later_vis");
          var j;
          for (j = 0; j < y.length; j++) {
            y[j].style.display = "inline";
          }
          course = val;
        }
        function submitter(){
          var number = document.getElementById("number").value;
          var section = document.getElementById("section").value;
          var email = document.getElementById("email").value;
          var email_body = course+" "+number+" "+section+" "+email;
          document.getElementById("dissapear").style.display = "none";
          document.getElementById("end_appear").style.display = "inline";
          document.getElementById("end_link").href = "https://mail.google.com/mail/?view=cm&fs=1&to=classnotifier123@gmail.com&su=ClassNotifierRequest&body="+email_body;
          document.getElementById("end_appear2").style.display = "inline";
          document.getElementById("end_appear3").style.display = "inline";
          document.getElementById("end_dis").style.display = "none";
          //document.getElementById("frm1").submit();
        }

     </script>
  </body>
</html>
