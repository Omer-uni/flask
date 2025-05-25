📌 Proje Başlığı
Flask Ticket Sistemi

🧾 Proje Tanıtımı
Bu proje, kullanıcıların destek talepleri (ticket) oluşturabildiği, görüntüleyebildiği ve yönetebildiği basit bir Flask tabanlı ticket sistemidir.

🌐 Proje Web Linki
🔗 https://flask-ticket-system-final.onrender.com

🚀 Proje Özellikleri
🔐 Kullanıcı kayıt ve giriş işlemleri

📚 Yeni ticket oluşturabilme

📝 Ticket’ları düzenleyebilme ve silebilme

📦 Veritabanı bağlantısı ile kalıcı veri saklama

⚙️ Kurulum ve Çalıştırma
✅ Gereksinimler
Bu projeyi çalıştırmak için bilgisayarınızda aşağıdaki yazılımların kurulu olması gerekir:

Python 3.x

Kullanılan kütüphaneler:

Flask

(Diğer kütüphaneler requirements.txt dosyasında mevcuttur.)

💡 Bu kütüphaneleri requirements.txt dosyasından şu komutla yükleyebilirsiniz:
pip install -r requirements.txt

🚀 Uygulamayı Başlatma
Terminal üzerinden aşağıdaki komutu çalıştırarak uygulamayı başlatabilirsiniz:

nginx
Kopyala
Düzenle
python app.py
Uygulama tarayıcınızda şu adreste çalışacaktır:
📍 http://127.0.0.1:5000/

📂 Proje Dosya Yapısı
bash
Kopyala
Düzenle
├── app.py                        # Ana Python uygulama dosyası
├── templates/                   # HTML şablonlarının bulunduğu klasör
│   ├── index.html               # Anasayfa
│   ├── login.html               # Giriş formu
│   ├── register.html            # Kayıt formu
│   ├── dashboard.html           # Ticket paneli
│   ├── create_ticket.html       # Ticket oluşturma sayfası
│   ├── edit_ticket.html         # Ticket düzenleme sayfası
│   ├── ticket_acildi.html       # Ticket açıldığını bildiren sayfa
│   └── ticket_detail.html       # Ticket detaylarının görüntülendiği sayfa
├── uploads/                     # Resim dosyalarının bulunduğu klasör
│   └── noname.png               # Ticket'a yerleştirilen varsayılan resim
├── requirements.txt             # Gerekli Python paketlerini içeren dosya
├── README.md                    # Bazı gerekli komutlar
├── instance/                    # Veritabanı dosyalarının bulunduğu klasör
│   └── site.db                  # Veritabanı dosyası
├── appjson.py                   # Verilerin JSON çıktısını üreten Python dosyası
├── users.json                   # Kullanıcı JSON çıktısı
└── tickets/                     # Ticket JSON çıktıları
🖼️ Ekran Görselleri / Kısa Demo
🎬 Kısa Demo
🔗 Google Drive Demo Linki
