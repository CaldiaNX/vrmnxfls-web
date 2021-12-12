@echo off
: Pythonの実行モジュールパスを指定
SET PATH=%PATH%;C:\Python\Python39

: 各ポートに割り当てたHTTPサーバを起動。
: サーバを終了する場合はコマンドプロンプトを閉じる。
start python vrmnxfls_server_5301.py
start python vrmnxfls_server_5302.py
start python vrmnxfls_server_5303.py

: レイアウトの列車IDを設定してWebブラウザを起動。
: 列車IDを変更したい場合は「slt1」のパラメータを変更。
: 不要なら頭に「rem 」を付けてコメントアウト。
: 外部操作の場合は「localhost」をグローバルIPアドレスに変更してQRコードなどで下記のURLを伝える。
start http://localhost:5301/cgi-bin/vrmnxfls_controller.py?slt1=10
start http://localhost:5302/cgi-bin/vrmnxfls_controller.py?slt1=20
start http://localhost:5303/cgi-bin/vrmnxfls_controller.py?slt1=30

exit /b 0
