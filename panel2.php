<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Загрузка</title>
    <link rel="stylesheet" href="load.css">
  </head>
  <body>
    <div class="loader"></div>
    <?php
    error_reporting(0);
    $connection = mysql_connect('localhost','root',"");
    mysql_select_db("camp");
    mysql_query("SET NAMES utf8");
    if($_SERVER['REQUEST_METHOD'] == 'POST') {
      $name = $_POST['name'];
      $text = $_POST['text'];

      $qresult = mysql_query("SELECT chatId FROM users WHERE name='$name'");
      while ($res=mysql_fetch_assoc($qresult)) {
        $tmp = $res['chatId'];

        $result1 = mysql_query("INSERT INTO achievements (chatId,text) VALUES
        ('$tmp','$text')");
      }
      $qresult1 = mysql_query("SELECT chatId FROM users WHERE chatId!=0");
      while ($res1=mysql_fetch_assoc($qresult1)) {
        $tmp1 = $res1['chatId'];
        file_get_contents("https://api.telegram.org/bot378193841:AAHlU0XYa_sCSrWZ1CNp_8BkKX0N_X28oME/sendMessage?chat_id=" .$tmp ."&text=" .$name ."получил(а) ачивку " .$text);
      }
    }
    header('Location: index.html');
    exit();
    ?>
  </body>
</html>
