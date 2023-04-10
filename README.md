# doujin-manager
用來管理同人誌的 django 網站

### 使用 python3.10.10 開發

### 前置
安裝需求的 packages
```bash
{user}:{path-to-doujin-manager}/doujin-manager/doujin_manager$ pip -r install requirement.txt
```

mysql 相關設定
1. 下載並安裝 mysql, 接著跑起來(有則跳過)
2. 創個 user 名字為 "user", 密碼為 "password"
3. 做個 new table 名為 "doujin-manager"
mysql 設定就完成了

初始化 django 需要的 db
```bash
{user}:{path-to-doujin-manager}/doujin-manager/doujin_manager$ python manage.py migrate
```

### 啟動
```bash
{user}:{path-to-doujin-manager}/doujin-manager/doujin_manager$ python manage.py runserver
```

### 透過 docker
```bash
{user}:{path-to-doujin-manager}/doujin-manager$ docker compose up -d
```
網站將會開在 localhost:8000

ref:
[API SPEC](https://app.swaggerhub.com/apis-docs/B850108CD/Doujinshi/1.0.0#/)
