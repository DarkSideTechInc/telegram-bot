<?php

$token = "YOUR_BOT_TOKEN";
$website = "https://api.telegram.org/bot".$token;

$update = file_get_contents('php://input');
$update = json_decode($update, TRUE);

$chatId = $update["message"]["chat"]["id"];
$message = $update["message"]["text"];
$message_id = $update["message"]["message_id"];
$sk = "YOUR_SK_HERE";

if (strpos($message, "/start") === 0) {
    sendMessage($chatId, "Hello! I'm your bot. How can I assist you today?", $message_id);
}

elseif ((strpos($message, "/sk") === 0)||(strpos($message, "!sk") === 0)||(strpos($message, ".sk") === 0)){
    sendMessage($chatId, "<b>Bot Is Now Checking If The SK is Working or Not...</b>", $message_id);
    $ch = curl_init();
    curl_setopt($ch, CURLOPT_URL, 'https://api.stripe.com/v1/accounts');
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
    curl_setopt($ch, CURLOPT_USERPWD, "$sk:");
    curl_setopt($ch, CURLOPT_FOLLOWLOCATION, 1);
    curl_setopt($ch, CURLOPT_HTTPHEADER, array(
        'Accept: application/json',
        'Content-Type: application/x-www-form-urlencoded',
    ));
    // Add this line to disable SSL certificate verification
    curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
    $result = curl_exec($ch);
    curl_close($ch);
    if (strpos($result, 'id')) {
        sendMessage($chatId, "<b>⋆ SK Checking Status:</b> Working ✅", $message_id);
    } else {
        sendMessage($chatId, "<b>⋆ SK Checking Status:</b> Not Working ❌", $message_id);
    }
}

function sendMessage($chatId, $message, $message_id){
    file_get_contents($GLOBALS['website'].'/sendmessage?chat_id='.$chatId.'&text='.$message.'&parse_mode=HTML&reply_to_message_id='.$message_id.'&disable_web_page_preview=true');
}
?>
