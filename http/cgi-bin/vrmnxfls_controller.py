import cgi
import sys
import io
import re
import datetime

# printで出力する内容をutf-8にする
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding = 'utf-8')
# ファイルの種類を定義
print('Content-Type: text/html; charset=UTF-8\n')
# テンプレート読込み
with open("vrmnxfls_controller.html", encoding="utf-8") as f:
    html_body = f.read()

# inputからパラメータを取得
form = cgi.FieldStorage()
# 初期値はここで指定
slt1 = form.getvalue('slt1', '')
spd1 = int(form.getvalue('spd1', 0))
rst = form.list

# 列車IDあり
if len(slt1) > 0:
    # FLS用コマンド作成
    text = ''
    # 点灯ボタン
    if len(form.getvalue('pwon1', '')) > 0:
        text = 'T\t{}\tSetPower\t1'.format(slt1)
    # 消灯ボタン
    elif len(form.getvalue('pwof1', '')) > 0:
        text = 'T\t{}\tSetPower\t0'.format(slt1)
    # 速度UP
    elif len(form.getvalue('up1', '')) > 0:
        spd1 = spd1 + 10
        if spd1 > 100:
            spd1 = 100
        text = 'T\t{}\tAutoSpeedCTRL\t50\t{}'.format(slt1, spd1 * 0.01)
    # 速度Down
    elif len(form.getvalue('dn1', '')) > 0:
        spd1 = spd1 - 10
        if spd1 < 0:
            spd1 = 0
        text = 'T\t{}\tAutoSpeedCTRL\t50\t{}'.format(slt1, spd1 * 0.01)
    # 方向転換
    elif len(form.getvalue('tn1', '')) > 0:
        spd1 = 0
        text = 'T\t{}\tTurn\t0'.format(slt1)
    # 警笛
    elif len(form.getvalue('hn1', '')) > 0:
        text = 'T\t{}\tPlayHorn\t0'.format(slt1)
    # VRMNXFLS用ファイル出力
    path = 'C:\\VRMNX\\read\\'
    ymds = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9))).strftime('%Y%m%d%H%M%S')
    file = path + ymds + '.txt'
    # ファイル出力
    with open(file, mode='w') as f:
        f.write(text)

# postする変数を入力
html_body = html_body.format(slt1, spd1, rst)
# HTML出力
print (html_body)
