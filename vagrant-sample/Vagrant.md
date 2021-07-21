##  リンク
* [公式](https://learn.hashicorp.com/tutorials/vagrant/getting-started-networking?in=vagrant/getting-started)
* [NWのまとめ](https://qiita.com/ftakao2007/items/0ec05c2ef3c14cdbea11)
* []()
* []()

##  コマンド
```sh
## bionic64というbox（VMのもと）からVagrantfileを生成
vagrant init hashicorp/bionic64 
## Vagrantfileをもとに環境を作成
vagrant up
vagrant destroy

## うごいているときにVagrantfileを編集したら、これでリロードできる
vagrant reload --provision

```
## 仕様
vagrantのゲストの/vagrantとhostマシンのVagrantfileがおいてあるディレクトリが同期している
