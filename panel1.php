<?php
    error_reporting(0);
    $connection = mysql_connect('localhost','root',"");
    mysql_select_db("camp");
    mysql_query("SET NAMES utf8");
    if($_SERVER['REQUEST_METHOD'] == 'POST') {
      $id = $_POST['id'];
      $name = $_POST['name'];
      $subjectId = $_POST['subject'];
      $teamId = $_POST['team'];
      $phone = $_POST['phone'];
      $password = $_POST['password'];
      $home = $_POST['home'];
      $result = mysql_query("INSERT INTO users (id, name, phone, home,
         subjectId, teamId, password)
       VALUES (NULL, '$name', '$phone', '$home', '$subjectId', '$teamId', '$password')");
       mysql_fetch_assoc($result);
    }
    header('Location: index.html');
    exit();
?>
