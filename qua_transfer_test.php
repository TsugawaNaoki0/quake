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
        #####################################
        // require_once('config.php');
        // echo $_POST['email_tra'];
        $email = $_POST['email_tra'];


        define('DSN', 'mysql:host=localhost;dbname=mail_list');
        define('DB_USER', 'root');
        define('DB_PASS', '19960701mysql');

        $pdo = new PDO('mysql:host=localhost;dbname=mail_list', 'root', '19960701mysql');
        //データベースへ接続、テーブルがない場合は作成

        // データーベースtestへ接続
        // 部品登録テーブルの部品名の値を降順に取得して$entryに格納
        $result_rows = $pdo->query('select * from mailDeta;');
        foreach ( $result_rows as $row ) {
            // テーブルの1行ごとに1つの配列として格納されている（$row）
            // その1行ごとの配列内で、列名をキーにした連想配列でデータが格納されている。
            $mail_list = $row['email']; // id列
            echo "'".$mail_list."'"." ";
            // echo "name: {$row['name']}"; // name列
        }


        // echo shell_exec("export LANG=ja_JP.UTF-8; python3 quake.py ".$mail_list);


        //POSTのValidate。
        // if (!$email = filter_var($_POST['email'], FILTER_VALIDATE_EMAIL)) {
        //   if (!$email = filter_var($email, FILTER_VALIDATE_EMAIL)) {
        //   echo '入力された値が不正です。';
        //   return false;
        // }


        ##############################

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
