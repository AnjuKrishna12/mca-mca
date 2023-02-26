<html>
<head>
<script type="text/javascript" >
function validateHTMlform()
{
  let form = document.StudenSignupForm;
   if( form.textnames.value == "" )
   {
     alert( "Enter Your First Name!" );
     form.textnames.focus() ;
     return;
   }
   if( form.lastnames.value == "" )
   {
     alert( "Enter Your Last Name!" );
     form.textnames.focus() ;
     return;
   }
  
   if( form.guardianname.value == "" )
   {
     alert( "Enter Your Guardians Name!" );
     form.guardianname.focus() ;
     return;
   }
  
   if( form.paddress.value == "" )
   {
     alert( "Enter Your Postal Address!" );
     form.paddress.focus() ;
     return;
   }
   if( form.personaladdress.value == "" )

   {
     alert( "Enter Your Personal Address!" );
     form.personaladdress.focus() ;
     return;
   }
 
    
   if( form.Course.value == "-1" )
   {
     alert( "Enter Your Course!" );
    
     return;
   }  
 
var email = form.emailid.value;
  atpos = email.indexOf("@");
  dotpos = email.lastIndexOf(".");
if (email == "" || atpos < 1 || ( dotpos - atpos < 2 ))
{
     alert("Enter your correct email ID")
     form.emailid.focus() ;
     return;
}
  if( form.dob.value == "" )
   {
     alert( "Enter your DOB!" );
     form.dob.focus() ;
     return;
   }
  if( form.mobileno.value == "" ||
           isNaN( form.mobileno.value) ||
           form.mobileno.value.length != 10 )
   {
     alert( "Enter your Mobile No. in the format 123." );
     form.mobileno.focus() ;
     return;
   }
   return( true );
}</script>

</head>
 
<body>
<form action="#" name="StudenSignupForm" onsubmit="return(validateHTMlform());">
 

 

<center><font size=4><b>Student Registration Form</b></font></center>

 

<table border ="2"><tr><td>First Name</td>
<td><input type=text name=textnames id="textname" size="30"></td>
</tr>
 
  <tr>
<td>
  Last Name</td>
<td><input type=text name=lastnames id="lastname" size="30"></td>
</tr>
  
<tr>
<td>Guardians Name</td>
<td><input type="text" name="guardianname" id="fathername"size="30"></td>
</tr>
 
 
<tr>
<td>Address</td>
<td><input type="text" name="personal_address"
id="personaladdress" size="30"></td>
</tr>
 
<tr>
<td>Gender</td>
<td><input type="radio" name="sex" value="male" size="10">Male
<input type="radio" name="sex" value="Female" size="10">Female</td>
</tr>

<tr>
<td>Course</td>
<td><select name="Course">
<option value="-1" selected>select..</option>
<option value="B.Tech">B.TECH</option>
<option value="MCA">MCA</option>
<option value="MBA">MBA</option>
<option value="BCA">BCA</option>
</select></td>
</tr>
<tr>
<td>student email</td>
<td><input type="text" name="email_id" id="emailid" size="30"></td>
</tr>
 
<tr>
<td>Date Of Birth</td>
<td><input type="text" name="date_of_birth" id="dob" size="30"></td>
</tr>
 
<tr>
<td>Mobile Number</td>
<td><input type="text" name="mobilenumber" id="mobile_no" size="30" ></td>
</tr>
<tr>
<td><input type="reset"></td><td>
<input type="submit" value="Submit Form" /></td>
</div></tr>
</form>
</body>
</html>
