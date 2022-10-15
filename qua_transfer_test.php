<!DOCTYPE html>
<html lang="ja">
 <head>
   <meta charset="utf-8">
   <link rel="stylesheet" href="./home.css">
   <title>HallowinGhost</title>
    <link rel="icon" href="./quake.png"><!-- タイトルにアイコンを設定 -->
    <link rel="apple-touch-icon" href="./quake.png"><!-- iphone のアイコンを設定 -->
 </head>
 <body>
    <div class="main">
      <link rel="stylesheet" href="./home.css">
      <div class="main">
        <br>
        <br>
        <br>
        <br>
        <br>
        <br>
        <br>
        <br>
        <br>
        <br>
        <div class="label">
          地震が発生しました[これはテストです]
        </div>
        <br>
        <br>
        <br>
        <br>
        <br>
        <br>
      <?php


        $time_from_python = shell_exec("export LANG=ja_JP.UTF-8; python3 times.py");
        // echo shell_exec("export LANG=ja_JP.UTF-8; python3 times.py");
        echo shell_exec("export LANG=ja_JP.UTF-8; python3 quake_test.py ");
        // echo $time_from_python;
       ?>

       <div class="timestamp">
         <?php echo $time_from_python
          ?>
          <br>
          <br>
          <br>
          <br>
          <br>

       </div>
      </div>

    </div>
 </body>
</html>
