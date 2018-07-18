<?php

paymails();


function paymails(){ 

$fname = $_POST['fname']; 
$lname = $_POST['lname']; 
$address1 = $_POST['address1']; 
$address2 = $_POST['address2']; 
$phone = $_POST['mobile']; 
$email_address = $_POST['email']; 
$city = $_POST['city']; 
$state = $_POST['state']; 
$zip = $_POST['zip']; 


$myemail = "rohit.scalable@gmail.com,scalableapplication@gmail.com,jay@ntxwinetours.com,marcus@dmtechsolutions.com" ;//<-----Put Your email address here.
if(empty($_POST['fname'])  || 
   empty($_POST['lname']) ||
 empty($_POST['mobile']) ||
 empty($_POST['email']) || 
   empty($_POST['address1'])||
   
    empty($_POST['city']) ||
 empty($_POST['state']) || 
   empty($_POST['zip'])
   )
{
    $errors .= "\n Error: all fields are required";
}
if (!preg_match(
"/^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,3})$/i", 
$email_address))
{
    $errors .= "\n Error: Invalid email address";
}


	//$to="info@dmtechsolutions.com,marcusdorris1@gmail.com";
	$to="rohit.scalable@gmail.com,scalableapplication@gmail.com,marcus@dmtechsolutions.com,jay@ntxwinetours.com";
	$sub="Wine Booking : ".$fname;
	
	$subject =$sub;
	//$message="Name: ".$text."<br> Email: ".$email."<br> Phone No: ".$_POST['phone']."<br> Message: ".$_POST['message'];
	//$message="Text: ".$text."<br />";
	
$message="You have received a new message <br><br> First Name:". $fname ."<br>Last Name: ".$lname." <br>phone: ".$phone. "<br> Email: ". 
  $email_address."<br>Address: ".$address1."  ".$address2."<br> City:".$city."<br> State:". $state ."<br>Zip: ".$zip."<br><b>Note: Please check PayPal Account for payment clearance from this client, also check tour type detail there.</b>";
	
$cleanedFrom=$email_address ;

	

//$cleanedFrom="scalableapplication@gmail.com";

	$headers = "From: " . $cleanedFrom . "\r\n";

	$headers .= "Reply-To: ". strip_tags($cleanedFrom) . "\r\n";

	$headers .= "MIME-Version: 1.0\r\n";

	$headers .= "Content-Type: text/html; charset=ISO-8859-1\r\n";

	$mail=@mail($to,$subject,$message,$headers);
	if($mail) {
//header('Location: bookingpaypal.html');	
	?>
		<script>alert("Email has been Send Successfully."); window.location="bookingpaypal.html"</script>

	<?php } else { ?>
		<script>alert("Error Occured !! Try again ..."); window.location="bookingpaypal.html"</script>
	<?php } ?>

<?php } ?>
?>