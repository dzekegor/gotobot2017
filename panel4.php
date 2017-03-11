<?php
    error_reporting(0);
    $connection = mysql_connect('localhost','root',"");
    mysql_select_db("camp");
    mysql_query("SET NAMES utf8");
    if($_SERVER['REQUEST_METHOD'] == 'POST') {

      $sobs = $_POST['sob'];
      print_r($sobs);

      $times = $_POST['time'];
      print_r($times);
      $res = mysql_query("DELETE FROM timetable WHERE 1");
      mysql_fetch_assoc($res);
      $s = "";
      $qresult = mysql_query("SELECT chatId FROM users");
      while ($res=mysql_fetch_assoc($qresult)) {
        $tmp = $res['chatId'];
        file_get_contents("https://api.telegram.org/bot378193841:AAHlU0XYa_sCSrWZ1CNp_8BkKX0N_X28oME/sendMessage?chat_id=" .$tmp ."&text=Расписание изменилось!");

      }
      for ($i=1; $i < count($sobs)+1; $i++) {
        $result = mysql_query("INSERT INTO timetable (time,event) VALUES
        ('$times[$i]','$sobs[$i]')");

        mysql_fetch_assoc($result);

        $s = "$times[$i] $sobs[$i]";
        $qresult = mysql_query("SELECT chatId FROM users");
        while ($res=mysql_fetch_assoc($qresult)) {
          $tmp = $res['chatId'];
          file_get_contents("https://api.telegram.org/bot378193841:AAHlU0XYa_sCSrWZ1CNp_8BkKX0N_X28oME/sendMessage?chat_id=" .$tmp ."&text=" .$s);

        }
      }

    }
    header('Location: /');
    exit();
?>
