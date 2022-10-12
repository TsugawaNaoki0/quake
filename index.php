<!DOCTYPE html>
<html lang="ja">
 <head>
   <meta charset="utf-8">
   <link rel="stylesheet" href="./../../home.css">
   <title>HallowinGhost</title>
    <link rel="icon" href="ghost.png"><!-- タイトルにアイコンを設定 -->
    <link rel="apple-touch-icon" href="icon.png"><!-- iphone のアイコンを設定 -->
 </head>
 <body>
    <div class="main">
            <br>
            <h1>地震速報</h1>
            <br>
            <br>
            <form action="./qua_transfer.php" method="post">
              <!-- <input type="textarea" name="confirm" value=""> -->
              <label for="confirm0"><h3>地震の有無</h3></label><br>
             　　地震あり：「There are some changes」<br>
             　　地震なし：「no change」<br>
              <input type="submit" value="-----" class="form">
            </form>
            <br>
            <form action="./qua_transfer.php" method="post">
              <!-- <input type="textarea" name="confirm" value=""> -->
              <label for="confirm0"><h3>地震発生ボタン（仮）</h3></label><br>
              <input type="submit" value="-----" class="form">
            </form>
            <br>
            <br>
    </div>
 </body>
</html>
