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
            <h1>リボ払い</h1>
            <br>
            ※ 1ヶ月を30日(1年を360日)として計算しています
            <br>
            <form action="./qua_transfer.php" method="post">
              <!-- <input type="textarea" name="confirm" value=""> -->
              <label for="confirm0"><h3>年利率</h3></label><br>
              <select name="confirm0" class="form">
                  <!-- <option value="blue">青</option> -->
                  <option value="0.10">10%</option>
              </select>
              <input type="submit" value="-----" class="form">
            </form>
            <br>
            <br>
    </div>
 </body>
</html>
