<?php
    error_reporting(0);
    $connection = mysql_connect('localhost','root',"");
    mysql_select_db("camp");
    mysql_query("SET NAMES utf8");
    if($_SERVER['REQUEST_METHOD'] == 'POST') {

      $questions = $_POST['question'];
      print_r($questions);

      $answers = $_POST['answer'];
      print_r($answers);

      $teams = $_POST['team'];
      print_r($teams);
      for ($i=1; $i < count($questions)+1; $i++) {
        $result = mysql_query("INSERT INTO quest (text,answer,teamId) VALUES
        ('$questions[$i]','$answers[$i]', '$teams[$i]')");

        mysql_fetch_assoc($result);
      }

    }
    header('Location: /');
    exit();
?>
