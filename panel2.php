<?php
    error_reporting(0);
    $connection = mysql_connect('localhost','root',"");
    mysql_select_db("camp");
    mysql_query("SET NAMES utf8");
    if($_SERVER['REQUEST_METHOD'] == 'POST') {
      $name = $_POST['name'];
      $text = $_POST['text'];
      $qresult1 = mysql_query("SELECT chatId FROM users WHERE name='$name'");
      while ($res1=mysql_fetch_assoc($qresult1)) {
        $tmp1 = $res1['chatId'];
        $result1 = mysql_query("INSERT INTO achievements (chatId,text) VALUES
        ('$tmp1','$text')");
        $result2 = mysql_query("INSERT INTO new_achievements (chatId,text) VALUES
        ('$tmp1','$text')");
      }

    }
    header('Location: /');
    exit();
    ?>
  </body>
</html>
