import http.server
# ポート番号を設定
server_address = ("", 5301)
# ハンドラを設定
handler_class = http.server.CGIHTTPRequestHandler
# サーバクラスを作成
server = http.server.HTTPServer(server_address, handler_class)
# ループ処理を実行
server.serve_forever()