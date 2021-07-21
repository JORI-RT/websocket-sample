## このリポジトリとは
scalabilityのあるwebsocketサーバーの検証のため、テトシスの備忘録さまのブログの内容を解析してみu
## 参考リンク
[main](https://www.tetsis.com/blog/pub-sub-websocket-scale-out-on-premise/)
[selinux解除](https://qiita.com/mattsun/items/470581ff34f87c7eb21d)
[]()
[]()
[]()
## ハマリポイント
### haproxyが正しくstartできない
selinuxをdisableにしないとhaproxyが正常にスタートしない
以下のようなエラーがでる
sudo systemctl status haproxy -l  
エラー内容
```sh
Jul 20 07:24:26 lb.local haproxy-systemd-wrapper[3420]: [ALERT] 200/072426 (3421) : parsing [/etc/haproxy/haproxy.cfg:65] : 'bind *:443' : unable to load SSL private key from PEM file '/etc/haproxy/server.pem'.
```
対処方法
[selinux解除](https://qiita.com/mattsun/items/470581ff34f87c7eb21d)
### docker-composeが起動しない
sudoコマンドでdocker-composeを起動する
sudo /usr/local/bin/docker-compose hogehoge
```
ERROR: Couldn't connect to Docker daemon at http+docker://localhost - is it running?
```


