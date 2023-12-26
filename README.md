# React, Django, mysql, nginx, それぞれ Docker でコンテナ化する。

学習として、実際に作成したアプリを書き残す。
Docker Container 内での HotReload を実現済み。

後ほど RestFramework をセットする。

## 使い方

SECRET_KEY には、適当なキーをセットする。

トップディレクトリにて下記のコマンドを実施。

```terminal
docker compose up -d
```

下記にアクセスする。（ポート番号 80）

http://localhost/

![起動後の画像](./assets/nginx-docker.png)

## Tips

#### HotReload

Docker 内で React をホットリロードするために、docker-compose 時にローカルのソースコードをコンテナと同期するようにしている。（docker-compose.yml - Volume を参照。）
これによってコンテナにマウントされたソースコードを永続的に保ち、ソースコードの改変時に即時に反映する。
