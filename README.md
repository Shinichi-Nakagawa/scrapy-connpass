# ScrapyでAPIをCallしてDBに保存するサンプル

## 何ができるのか

* [connpassのAPI](https://connpass.com/about/api/)をCall
* 取得したイベント(勉強会)データをDB(SQLite3)に保存

## 動作環境

* gitクライアント(何でもOK)
    * ソースコードを取得するために使う
    * 面倒くさい方は直接ダウンロードしてもらってもOK
* Python 3系の最新Ver
    * 3.6以上を推奨
    * 試してはいませんが,3.3.x以上なら動くと思う
* Scrapyのインストールが必要(後述)
    * 1.4.0で検証(作成時点の最新バージョン)
* MacOS Sierra(10.12.6)
    * 上記のPythonバージョンおよびScrapyバージョンであればOS関係なく動くハズ

## セットアップ

### 1. リポジトリをclone or ダウンロードする

#### クローンの場合

```bash
$ git clone git@github.com:Shinichi-Nakagawa/scrapy-connpass.git
```

#### ダウンロードの場合

```bash
$ wget https://github.com/Shinichi-Nakagawa/scrapy-connpass/archive/master.zip
$ unzip master.zip
```


### 2. Pythonをインストール

* [ダウンロードサイト(公式)](https://www.python.org/downloads/)
* お使いのOS・プラットフォームに合わせてお使いください
* (繰り返しになりますが)Python 3.6以上が推奨です！

### 3. Scrapyをインストール

```bash
$ pip install scrapy
```

## 使い方

### ディレクトリに移動

Scrapyのエンドポイントにcdします.

```bash
$ cd scrapy-connpass/connpass
```

なお,ダウンロードで手に入れた人は最初のディレクトリ名が変わるので注意

```bash
$ cd scrapy-connpass-master/connpass
```

### イベント情報を取得

scrapyのコマンドで取得します.

初回実施の時はDBファイル(connpass.db)が生成され,同時にSchemeも作成されます.

例として,作者(shinyorke)が直近で参加した勉強会(Max100件,更新順)を取得する場合はこのようなコマンドになります.

```bash
$ scrapy crawl api -a nickname=shinyorke -a count=100 -a order=1
```

### オプションについて

[connpassのAPIリファレンス](https://connpass.com/about/api/)の「検索クエリ」に対応しています.

可変なのでいくつでも指定可能です.

```bash
$ scrapy crawl api -a {クエリ名}={クエリの内容}
```

### 戻り値について

* sqlite3の「connpass.db」に保存されます.
* テーブル名はevent
* スキーマは[connpassのAPIリファレンス](https://connpass.com/about/api/)の「レスポンス」の「events」配列に準じています.