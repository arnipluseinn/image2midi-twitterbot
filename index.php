<?php

// Time
date_default_timezone_set("GMT");
$today = date("H:i:s")." - ".date("j, n, Y"); 

// Geo
$user_ip = getenv('REMOTE_ADDR');
$geo = unserialize(file_get_contents("http://www.geoplugin.net/php.gp?ip=$user_ip"));
$country = $geo["geoplugin_countryName"];
$city = $geo["geoplugin_city"];

// Write + Close
$file = fopen("ip.txt","a");
$ip=$today." - ".$user_ip." - ".$city." - ".$_SERVER['HTTP_USER_AGENT'].PHP_EOL;
fwrite($file,$ip);
fclose($file);
?> 
