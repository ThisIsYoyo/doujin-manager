# doujin-manager
用來管理同人誌的 django 網站

### 使用 python3.10.10 開發

### 前置
安裝需求的 packages
```bash
{user}:{path-to-doujin-manager}/doujin-manager/doujin_manager$ pip -r install requirement.txt
```

做個 django 需要的 db
```bash
{user}:{path-to-doujin-manager}/doujin-manager/doujin_manager$ python manage.py migrate
```

### 啟動
```bash
{user}:{path-to-doujin-manager}/doujin-manager/doujin_manager$ python manage.py runserver
```

ref:
[API SPEC](https://app.swaggerhub.com/apis-docs/B850108CD/Doujinshi/1.0.0#/)
