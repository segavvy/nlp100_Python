#!/bin/sh

# CGIHTTPRequestHandlerをハンドラとしてWebサーバー起動
python -m http.server --cgi 8000

