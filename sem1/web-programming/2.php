<html>
    <head>
        <title>Bill Invoice</title>
  </head>
  <body>
    <form action="" method="POST" >
      <h1><center>ENTER THE DETAILS</center></h1>
      <h3>Enter item name<input type=text name=itemname></h3>
      <h3>Enter item quantity<input type=text name=itemquan></h3>
      <h3>Enter item rate<input type=text name=itemrate></h3>
      <input type="submit" />
    </form>
  </body>
</html>


<?php
if($_POST)
{
 $itemname=$_POST['itemname'];
 $itemquan=$_POST['itemquan'];
 $itemrate=$_POST['itemrate'];
 $iname=explode(",",$itemname);
 $iquan=explode(",",$itemquan);
 $irate=explode(",",$itemrate);
 $amt=0;
 $n = count($iname);
 for($x=0;$x<$n;$x++)
 {
   $amt+=$irate[$x]*$iquan[$x];
 }
 echo"<table align=center border=2>";
 echo "<tr><td>" . "item name" . "</td><td>" . "item quantity" . "</td><td>" . "item rate" . "</td></tr>";
 
 for($x=0;$x<$n;$x++)
 {
   echo"<tr><td>".$iname[$x]."</td><td>".$iquan[$x]."</td><td>".$irate[$x]."</td></tr>";
 }
 echo"<tr><td>"."amount"."</td><td>"."$amt"."</td></tr>";
 echo"</table>";
}
?>
