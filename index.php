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
            <br>
            <br>
            <br>
            <p class="title">
             地震速報
            </p>
            <form action="./qua_transfer_test.php" method="post">
              <!-- <input type="textarea" name="confirm" value=""> -->
              <label for="confirm0" class="label">地震発生テストボタン（仮）</label>
              <br>
              <br>
              <br>
              <input type="submit" value="-----" class="form">
            </form>
            <br>
            <hr>
            <h1>メールアドレス登録</h1>
            <details>
              <br>
              <br>
              <br>
              <br>
              <br>
              <form action="./mail_transfer.php" method="post" class="login">
                <!-- <label for="email">E-MAIL</label> -->
                <input type="email" name="email" class="registration" placeholder="E-MAIL" required>
                <br>
                <br>
                <input type="submit" value="-----" class="login">
                <br>
                <br>
                <!-- <input type="checkbox" name="q2" value=""> -->
                <!-- <label for="q2"><a href="./../../riyoukiyaku.html">利用規約</a>に同意する</label> -->
                <!-- <p>※パスワードは半角英数字をそれぞれ１文字以上含んだ、<br>
                  ８文字以上で設定してください。</p> -->
                </form>
            </details>
            <br>
            <br>
            <br>
    </div>
 </body>
</html>
