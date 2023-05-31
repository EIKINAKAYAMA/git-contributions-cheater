# git-contributions-cheater

# Processs
1. 指定した日に、指定した分だけcontributesを生成するようなバッチを作成する。
2. Github APIから指定されたユーザーのContributionsを取得。
3. 完成系の文字の必要Contributesを自動で計算し、1を実行。
   ここまでをモジュール化
4. 定期実行で、上記のリポジトリを自動で削除し、自動で作成しバッチを実行するようにする。
5. 毎日実行させる。