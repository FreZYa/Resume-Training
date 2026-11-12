# Resume Site

[![CI](https://github.com/FreZYa/Resume-Training/actions/workflows/ci.yml/badge.svg)](https://github.com/FreZYa/Resume-Training/actions/workflows/ci.yml)

Django ile yazılmış, içeriği tamamen admin panelinden yönetilen kişisel CV ve portfolyo sitesi.

## Özellikler

- **Admin'den yönetilen içerik:** site başlığı, banner metinleri, logo ve favicon, yetenekler (yüzdeli), iş deneyimi, eğitim ve sosyal medya linkleri
- **Doküman linkleri:** CV gibi dosyalar admin'den yüklenir, menüde kısa bir linkle (`/<slug>/`) yayınlanır
- **İletişim formu:** AJAX ile gönderilir. Mesaj veritabanına kaydedilir ve site sahibine e-posta olarak iletilir (reply-to gönderenin adresidir)
- **Boş veritabanında çalışma:** ilk kurulumda ayar girilmemiş olsa da sayfalar açılır
- **Docker ile geliştirme ortamı** ve GitHub Actions'ta testler

## Teknolojiler

Python 3.11, Django 5.2, django-environ, SQLite, Docker, GitHub Actions

## Kurulum

### Docker ile

```bash
git clone https://github.com/FreZYa/Resume-Training.git
cd Resume-Training
cp resume/docker.env.example resume/docker.env   # değerleri düzenleyin
docker compose up --build
```

Site `http://localhost:8000` adresinde açılır. Admin kullanıcısı oluşturmak için:

```bash
docker compose exec app python manage.py createsuperuser
```

Ardından `/admin/` üzerinden içerik girin.

### Docker olmadan

```bash
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp resume/docker.env.example resume/.env
python manage.py migrate
python manage.py runserver
```

## Ortam değişkenleri

| Değişken | Açıklama |
|---|---|
| `SECRET_KEY` | Django secret key |
| `DEBUG` | `True` / `False` |
| `ALLOWED_HOSTS` | Virgülle ayrılmış host listesi |
| `CSRF_TRUSTED_ORIGINS` | Virgülle ayrılmış origin listesi |
| `EMAIL_URL` | SMTP adresi. Geliştirmede `consolemail://` e-postaları konsola basar |
| `DEFAULT_FROM_EMAIL` | İletişim formundan gelen mesajların gönderileceği adres |

## Testler

```bash
python manage.py test
```
