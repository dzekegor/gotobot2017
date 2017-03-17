<?php
  error_reporting(0);
  $connection = mysql_connect('localhost','root',"");
  mysql_select_db("camp");
  mysql_query("SET NAMES utf8");

  if($_SERVER['REQUEST_METHOD'] == 'POST') {
    $quick = $_POST['quick'];
    $qresult = mysql_query("SELECT chatId FROM users WHERE chatId<>0");
    while ($res=mysql_fetch_assoc($qresult)) {
      $tmp = $res['chatId'];
      file_get_contents("https://api.telegram.org/bot378193841:AAHlU0XYa_sCSrWZ1CNp_8BkKX0N_X28oME/sendMessage?chat_id=" .$tmp ."&text=" .$quick);

    }

  }
  header('Location: /');
  exit();

?>
