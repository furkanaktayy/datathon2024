import pandas as pd


# Specify the data types for the columns with mixed types
dtype_spec = {
    'column_13': str,
    'column_15': str,
    'column_19': str,
    'column_30': str,
    'column_32': str,
    'column_37': str,
    'column_41': str,
    'column_42': str
}

# Load the data
df = pd.read_csv('train_data_2022.csv', dtype=dtype_spec, low_memory=False)

# Fill missing values with 0
df = df.fillna(0)
df = df.dropna(subset=['Dogum Tarihi'])

# Drop unnecessary columns
columns_to_drop = ['Spor Dalindaki Rolunuz Nedir?','Ikametgah Sehri','Dogum Tarihi','Ingilizce Seviyeniz?','Burslu ise Burs Yuzdesi','Dogum Yeri','Baska Kurumdan Aldigi Burs Miktari', 'Lise Adi', 'Lise Adi Diger', 'Lise Sehir', 'Lise Bolum Diger', 'Lise Mezuniyet Notu', 'Burs Aldigi Baska Kurum', 'Uye Oldugunuz Kulubun Ismi', "Hangi STK'nin Uyesisiniz?", 'Girisimcilikle Ilgili Deneyiminizi Aciklayabilir misiniz?', 'Daha Önceden Mezun Olunduysa, Mezun Olunan Üniversite', 'id']
df = df.drop(columns=columns_to_drop, errors='ignore')
df = df.dropna(subset=['Universite Adi'])

# Define the variables for mapping
sektor_mapping = {
    'Özel Sektör': 3,
    '-': 0,
    'Kamu': 2,
    'Diğer': 1
}

lisetip = {
    'Devlet': 1,
    'Özel': 0,
}

egitim_mapping = {
    'Eğitimi yok': 0,
    'İlkokul': 1,
    'Ortaokul': 2,
    'Lise': 3,
    'Üniversite': 4,
    'Yüksek Lisans': 5,
    'Doktora': 6
}

lise_bolumu_mapping = {
    'Eşit Ağırlık': 0,
    'Sözel': 1,
    'Sayısal': 2,
    'Dil': 3
}

bolum_mapping={'Diğer': 0, 'Uluslararası Ticaret': 1, 'Uluslararası İlişkiler': 2, 'Bilgisayar Mühendisliği': 3, 'Mimarlık': 4, 'Ekonomi': 5, 'İngilizce Öğretmenliği': 6, 'Kimya': 7, 'Hukuk': 8, 'Tıp': 9, 'Elektrik-Elektronik Mühendisliği': 10, 'Siyaset Bilimi ve Uluslararası İlişkiler': 11, 'İşletme': 12, 'Turizm İşletmeciliği': 13, 'Özel Eğitim Öğretmenliği': 14, 'Psikoloji': 15, 'Diş Hekimliği': 16, 'İşletme Mühendisliği': 17, 'Turizm İşletmeciliği ve Otelcilik': 18, 'İngiliz Dili ve Edebiyatı': 19, 'Bilgisayar Bilimleri': 20, 'Endüstri Mühendisliği': 21, 'İç Mimarlık': 22, 'Eczacılık': 23, 'Kontrol ve Otomasyon Mühendisliği': 24, 'Medya ve Görsel Sanatlar': 25, 'Sosyoloji': 26, 'Türk Dili ve Edebiyatı Öğretmenliği': 27, 'Endüstri Ürünleri Tasarımı': 28, 'Yönetim Bilişim Sistemleri': 29, 'Astronomi ve Uzay Bilimleri': 30, 'Makine Mühendisliği': 31, 'Grafik': 32, 'İlahiyat': 33, 'Kimya Mühendisliği': 34, 'Rehberlik ve Psikolojik Danışmanlık': 35, 'Uçak Mühendisliği': 36, 'İnşaat Mühendisliği': 37, 'Gazetecilik': 38, 'Yönetim Bilimleri': 39, 'İktisat': 40, 'Coğrafya': 41, 'Halkla İlişkiler ve Reklamcılık': 42, 'Almanca, İngilizce Mütercim ve Tercümanlık': 43, 'Okul Öncesi Öğretmenliği': 44, 'Moleküler Biyoloji ve Genetik': 45, 'Görsel İletişim Tasarımı': 46, 'Sınıf Öğretmenliği': 47, 'Fizyoterapi ve Rehabilitasyon': 48, 'İngilizce Mütercim ve Tercümanlık': 49, 'İç Mimarlık ve Çevre Tasarımı': 50, 'Matematik Mühendisliği': 51, 'Elektronik ve Haberleşme Mühendisliği': 52, 'İslami İlimler': 53, 'Veteriner': 54, 'Mekatronik Mühendisliği': 55, 'Enerji Mühendisliği': 56, 'Hemşirelik': 57, 'Türkçe Öğretmenliği': 58, 'Petrol ve Doğalgaz Mühendisliği': 59, 'Felsefe': 60, 'Malzeme Bilimi ve Nano Mühendislik': 61, 'Malzeme Bilimi ve Mühendisliği': 62, 'Bankacılık ve Sigortacılık': 63, 'Matematik': 64, 'Geomatik Mühendisliği': 65, 'Şehir ve Bölge Planlama': 66, 'Elektrik Mühendisliği': 67, 'Beslenme ve Diyetetik': 68, 'Yeni Medya ve İletişim': 69, 'Dil ve Konuşma Terapisi': 70, 'Otomotiv Mühendisliği': 71, 'Beden Eğitimi ve Spor Öğretmenliği': 72, 'Elektronik Mühendisliği': 73, 'Türk Dili ve Edebiyatı': 74, 'Endüstriyel Tasarım': 75, 'Metalurji ve Malzeme Mühendisliği': 76, 'Halkla İlişkiler': 77, 'Bilgisayar ve Öğretim Teknolojileri Öğretmenliği': 78, 'Siyaset Bilimi ve Kamu Yönetimi': 79, 'Biyoloji': 80, 'Sosyal Hizmet': 81, 'İletişim ve Tasarımı': 82, 'Çevre Mühendisliği': 83, 'Moleküler Biyoteknoloji': 84, 'Egzersiz ve Spor Bilimleri': 85, 'Bilgisayar Bilimi ve Mühendisliği': 86, 'Mütercim-Tercümanlık (Rusça)': 87, 'Havacılık ve Uzay Mühendisliği': 88, 'Dijital Oyun Tasarımı': 89, 'Fen Bilgisi Öğretmenliği': 90, 'Çocuk Gelişimi': 91, 'Havacılık Elektrik ve Elektroniği': 92, 'Yazılım Mühendisliği': 93, 'Arkeoloji ve Sanat Tarihi': 94, 'Maden Mühendisliği': 95, 'Gemi ve Deniz Teknolojisi Mühendisliği': 96, 'Fizik': 97, 'Fizik Öğretmenliği': 98, 'Maliye': 99, 'Sağlık Yönetimi': 100, 'Biyomühendislik': 101, 'Bilişim Sistemleri Mühendisliği': 102, 'Fizik Mühendisliği': 103, 'Biyomedikal Mühendisliği': 104, 'Moleküler Biyoloji, Genetik ve Biyomühendislik': 105, 'Gemi İnşaatı ve Gemi Makineleri Mühendisliği': 106, 'Çalışma Ekonomisi ve Endüstri İlişkileri': 107, 'Denizcilik İşletmeleri Yönetimi': 108, 'İlköğretim Matematik Öğretmenliği': 109, 'Gastronomi ve Mutfak Sanatları': 110, 'Yeni Medya': 111, 'Biyoloji Öğretmenliği': 112, 'Spor Bilimleri': 113, 'Deniz Ulaştırma İşletme Mühendisliği': 114, 'Gıda Mühendisliği': 115, 'Uluslararası Ticaret ve İşletmecilik': 116, 'Endüstriyel Tasarım Mühendisliği': 117, 'Alman Dili ve Edebiyatı': 118, 'Enerji Sistemleri Mühendisliği': 119, 'Jeofizik Mühendisliği': 120, 'İletişim Tasarımı': 121, 'İletişim': 122, 'Hemşirelik ve Sağlık Hizmetleri': 123, 'Tarih': 124, 'Tıp Mühendisliği': 125, 'Reklamcılık': 126, 'Malzeme Bilimi ve Teknolojileri': 127, 'Sermaye Piyasası': 128, 'Radyo,Televizyon ve Sinema': 129, 'Arap Dili ve Edebiyatı': 130, 'Ekonometri': 131, 'İmalat Mühendisliği': 132, 'İstatistik': 133, 'Uluslararası Ticaret ve Lojistik': 134, 'Acil Yardım ve Afet Yönetimi': 135, 'Kamu Yönetimi': 136, 'Görsel Sanatlar ve Görsel İletişim Tasarımı': 137, 'Halkla İlişkiler ve Tanıtım': 138, 'Pazarlama': 139, 'Bilgi Güvenliği Teknolojisi': 140, 'Finans ve Bankacılık': 141, 'Uçak ve Uzay Mühendisliği': 142, 'İşletme Yönetimi': 143, 'Uçak Bakım ve Onarım': 144, 'Ebelik': 145, 'Mütercim-Tercümanlık (İngilizce)': 146, 'Tarım Makineleri ve Teknolojileri Mühendisliği': 147, 'Girişimcilik': 148, 'Tekstil Mühendisliği': 149, 'Tarımsal Biyoteknoloji': 150, 'Uluslararası Ticaret ve Finansman': 151, 'Ergoterapi': 152, 'Jeoloji Mühendisliği': 153, 'Almanca Mütercim ve Tercümanlık': 154, 'Kore Dili ve Edebiyatı': 155, 'Sigortacılık': 156, 'Arapça Mütercim ve Tercümanlık': 157, 'Biyokimya': 158, 'Muhasebe': 159, 'Biyosistem Mühendisliği': 160, 'Havacılık Yönetimi': 161, 'Uluslararası Lojistik Yönetimi': 162, 'Resim': 163, 'Harita Mühendisliği': 164, 'Peyzaj Mimarlığı': 165, 'Yazılım Geliştirme': 166, 'Siyaset Bilimi': 167, 'Müzik Bilimleri': 168, 'Turizm Rehberliği': 169, 'Sosyal Bilgiler Öğretmenliği': 170, 'Yerel Yönetimler': 171, 'Endüstri ve Sistem Mühendisliği': 172, 'Mekatronik Sistemler Mühendisliği': 173, 'Bahçe Bitkileri': 174, 'Kültür ve İletişim Bilimleri': 175, 'Tarım Ekonomisi': 176, 'Gastronomi': 177, 'Amerikan Kültürü ve Edebiyatı': 178, 'Odyoloji': 179, 'Aktüerya ve Risk Yönetimi': 180, 'Uluslararası Ticaret ve Finans': 181, 'Yapay Zeka Mühendisliği': 182, 'Reklam Tasarımı ve İletişimi': 183, 'Matematik Öğretmenliği': 184, 'Grafik Tasarımı': 185, 'Mütercim Tercümanlık (İngilizce, Fransızca, Türkçe)': 186, 'Uzay Mühendisliği': 187, 'Fransızca Öğretmenliği': 188, 'Mütercim-Tercümanlık (Almanca)': 189, 'Kimya-Biyoloji Mühendisliği': 190, 'Bankacılık ve Finans': 191, 'Aile ve Tüketici Bilimleri': 192, 'Resim İş Öğretmenliği': 193, 'Kimya Öğretmenliği': 194, 'Lojistik Yönetimi': 195, 'Genetik ve Biyomühendislik': 196, 'İletişim ve Tasarım': 197, 'Çeviribilim': 198, 'Spor Yöneticiliği': 199, 'Bilgisayar ve Yazılım Mühendisliği': 200, 'Antrenörlük': 201, 'Türk Müziği': 202, 'Gemi Makineleri İşletme Mühendisliği': 203, 'İşletme Enformatiği': 204, 'Ekonomi ve Finans': 205, 'Sinema ve Televizyon': 206, 'Antrenörlük Eğitimi': 207, 'Medya ve İletişim': 208, 'Fotoğraf': 209, 'Opera': 210, 'Sigortacılık ve Sosyal Güvenlik': 211, 'İletişim Tasarımı ve Yönetimi': 212, 'Arp': 213, 'Uçak Gövde ve Motor Bakımı': 214, 'Yunan Dili ve Edebiyatı': 215, 'Uluslararası Lojistik ve Taşımacılık': 216, 'Müzikoloji': 217, 'Bilgisayar Teknolojisi ve Bilişim Sistemleri': 218, 'Basım Teknolojileri': 219, 'Aktüerya': 220, 'Heykel': 221, 'Biyoenformatik ve Genetik': 222, 'Bitki Koruma': 223, 'Görsel Sanatlar': 224, 'Rekreasyon Yönetimi': 225, 'İnsan Kaynakları Yönetimi': 226, 'Basın ve Yayın': 227, 'Radyo ve Televizyon': 228, 'Sanat Tarihi': 229, 'Halı, Kilim ve Eski Kumaş Desenleri': 230, 'Orman Mühendisliği': 231, 'Uluslararası Girişimcilik': 232, 'Su Bilimleri ve Mühendisliği': 233, 'Çağdaş Türk Lehçeleri ve Edebiyatları': 234, 'Drama ve Oyunculuk': 235, 'Gümrük İşletme': 236, 'İstatistik ve Bilgisayar Bilimleri': 237, 'Fars Dili ve Edebiyatı': 238, 'Nükleer Enerji Mühendisliği': 239, 'Pilotaj': 240, 'Engellilerde Egzersiz ve Spor Bilimleri': 241, 'Gıda Teknolojisi': 242, 'Elektronik Ticaret ve Yönetimi': 243, 'Meteoroloji Mühendisliği': 244, 'Bankacılık': 245, 'Arkeoloji': 246, 'Kültür Varlıklarını Koruma ve Onarım': 247, 'Moda Tasarımı': 248, 'Bilgi ve Belge Yönetimi': 249, 'Rekreasyon': 250, 'Tarih Öğretmenliği': 251, 'Uçak Gövde-Motor Bakım': 252, 'Lojistik': 253, 'Arapça Öğretmenliği': 254, 'Muhasebe ve Finans Yönetimi': 255, 'Grafik Resimleme ve Baskı': 256, 'Grafik Tasarım': 257, 'Mütercim-Tercümanlık (Fransızca)': 258, 'Teknoloji ve Bilgi Yönetimi': 259, 'Biyoteknoloji': 260, 'Rusça Mütercim ve Tercümanlık': 261, 'İş Sağlığı ve Güvenliği': 262, 'Coğrafya Öğretmenliği': 263, 'Kompozisyon ve Şeflik': 264, 'Orman Endüstrisi Mühendisliği': 265, 'Tapu Kadastro': 266, 'Su Ürünleri Mühendisliği': 267, 'Felsefe Grubu Öğretmenliği': 268, 'Aktüerya Bilimleri': 269, 'Karşılaştırmalı Edebiyat': 270, 'Toprak Bilimi ve Bitki Besleme': 271, 'Ayakkabı Tasarımı ve Üretimi': 272, 'İngilizce, Fransızca Mütercim ve Tercümanlık': 273, 'Almanca Öğretmenliği': 274, 'Biyoteknoloji ve Moleküler Biyoloji': 275, 'Strateji ve Güvenlik (Askeri Yükseköğretim Kurumları)': 276, 'Farsça Mütercim ve Tercümanlık': 277, 'İşletme-Ekonomi': 278, 'Mütercim-Tercümanlık': 279, 'Fransız Dili ve Edebiyatı': 280, 'Uluslararası İşletmecilik ve Ticaret': 281, 'Bileşik Sanatlar': 282, 'Polimer Malzeme Mühendisliği': 283, 'Tekstil': 284, 'Klasik Arkeoloji': 285, 'Polimer Mühendisliği': 286, 'İletişim Bilimleri': 287, 'Organik Tarım İşletmeciliği': 288, 'Seyahat İşletmeciliği ve Turizm Rehberliği': 289, 'Çin Dili ve Edebiyatı': 290, 'Tarla Bitkileri': 291, 'İspanyol Dili ve Edebiyatı': 292, 'Müzik': 293, 'Seramik ve Cam': 294, 'Adli Bilişim Mühendisliği': 295, 'Uluslararası Finans ve Bankacılık': 296, 'Oyunculuk': 297, 'Cevher Hazırlama Mühendisliği': 298, 'Gerontoloji': 299, 'Rus Dili ve Edebiyatı': 300, 'Seramik': 301, 'Bilişim Sistemleri ve Teknolojileri': 302, 'El Sanatları': 303, 'Fransızca Mütercim veTercümanlık': 304, 'Astronomi ve Astrofizik': 305, 'Ağaç İşleri Endüstri Mühendisliği': 306, 'Mütercim ve Tercümanlık': 307, 'Resim-İş Öğretmenliği': 308, 'Yiyecek ve İçecek İşletmeciliği': 309, 'İslam İktisadı ve Finans': 310, 'Zootekni': 311, 'Ulaştırma ve Lojistik': 312, 'Latin Dili ve Edebiyatı': 313, 'Turizm ve Otelcilik': 314, 'Enerji Yönetimi': 315, 'Adli Bilimler': 316, 'Çizgi Film ve Animasyon': 317, 'Nanoteknoloji Mühendisliği': 318, 'İngiliz Dil Bilimi': 319, 'Makine ve İmalat Mühendisliği': 320, 'Uluslararası Ticaret ve Lojistik Yönetimi': 321, 'Optik ve Akustik Mühendisliği': 322, 'Raylı Sistemler Mühendisliği': 323, 'Uzay ve Uydu Mühendisliği': 324, 'Hidrojeoloji Mühendisliği': 325, 'Müzik Öğretmenliği': 326, 'Yaban Hayatı Ekolojisi ve Yönetimi': 327, 'Restorasyon ve Konservasyon': 328, 'Görsel Sanatlar Öğretmenliği': 329, 'İletişim Sanatları': 330, 'Matematik ve Bilgisayar Bilimleri': 331, 'Mütercim-Tercümanlık (Arapça)': 332, 'Bilim Tarihi': 333, 'Muhasebe Bilgi Sistemleri': 334, 'Ortez-Protez': 335, 'Perfüzyon': 336, 'Uzay Bilimleri ve Teknolojileri': 337, 'Tekstil ve Moda Tasarımı': 338, 'Müzik Teknolojileri': 339, 'Hayvansal Üretim ve Teknolojileri': 340, 'Uluslararası Çalışmalar': 341, 'Yeni Medya ve Gazetecilik': 342, 'Sanat Yönetimi': 343, 'Ses Eğitimi': 344, 'Tarımsal Genetik Mühendisliği': 345, 'Elektronik Ticaret ve Teknoloji Yönetimi': 346, 'Mütercim Tercümanlık (Almanca/İngilizce)': 347, 'Uluslararası İşletme Yönetimi': 348, 'Görsel İletişim': 349, 'Film Tasarım ve Yazarlık': 350, 'Gayrimenkul Geliştirme ve Yönetimi': 351, 'Piyano': 352, 'Kurgu-Ses ve Görüntü Yönetimi': 353, 'Çalgı Eğitimi': 354, 'Televizyon Haberciliği ve Programcılığı': 355, 'Moda ve Tekstil Tasarımı': 356, 'Antropoloji': 357, 'Süt Teknolojisi': 358, 'Malzeme Bilimi ve Nanoteknoloji Mühendisliği': 359, 'Sahne Tasarımı': 360, 'Eski Yunan Dili ve Edebiyatı': 361, 'Fotonik': 362, 'İşletme Bilgi Yönetimi': 363, 'Film Tasarımı ve Yazarlığı': 364, 'Japonca Öğretmenliği': 365, 'Türk Müziği Temel Bilimler': 366, 'Güvenlik Yönetimi (Askeri Yükseköğretim Kurumları)': 367, 'Yapay Zeka ve Veri Mühendisliği': 368, 'Balıkçılık Teknolojisi Mühendisliği': 369, 'Türk Halkbilimi': 370, 'Uluslararası Finans': 371, 'Dilbilim': 372, 'Çeviribilimi': 373, 'Temel Bilimler': 374, 'Geleneksel Türk Sanatları': 375, 'Takı Tasarımı': 376, 'Müzik (Piyano, Yaylı Çalgılar, Nefesli Çalgılar ve Vurma Çalgılar, Şan, Teori-Kompozisyon)': 377, 'Ortez ve Protez': 378, 'Sanat ve Kültür Yönetimi': 379, 'İngiliz Dilbilimi': 380, 'Azerbaycan Türkçesi ve Edebiyatı': 381, 'Protohistorya ve Önasya Arkeolojisi': 382, 'Grafik Sanatları': 383, 'Turizm ve Otel İşletmeciliği': 384, 'Muhasebe ve Denetim': 385, 'Japon Dili ve Edebiyatı': 386}

universite_adlari = {
    1 : ["İHSAN DOĞRAMACI BİLKENT","İhsan Doğramacı Bilkent Üniversitesi","İHSAN DOĞRAMACI BİLKENT ÜNİVERSİTESİ"],
    2 : ["ULUSLARARASI KIBRIS ÜNİVERSİTESİ","Uluslararası Kıbrıs Üniversitesi"],
    3 : ["İSTANBUL ŞEHİR ÜNİVERSİTESİ","İstanbul Şehir Üniversitesi"],
    4 : ["TURGUT ÖZAL ÜNİVERSİTESİ","Turgut Özal Üniversitesi","MALATYA TURGUT ÖZAL ÜNİVERSİTESİ","Malatya Turgut Özal Üniversitesi"],
    5 : ["İSTANBUL TİCARET ÜNİVERSİTESİ","İstanbul Ticaret Üniversitesi"],
    6 : ["İSTANBUL MEDİPOL ÜNİVERSİTESİ","İstanbul Medipol Üniversitesi"],
    7 : ["FATİH SULTAN MEHMET VAKIF","FATİH SULTAN MEHMET VAKIF ÜNİVERSİTESİ","Fatih Sultan Mehmet Vakıf Üniversitesi","Fatih Sultan Mehmet Üniversitesi"],
    8 : ["BAHÇEŞEHİR ÜNİVERSİTESİ","Bahçeşehir Üniversitesi"],
    9 : ["NUH NACİ YAZGAN ÜNİVERSİTESİ","Nuh Naci Yazgan Üniversitesi"],
    10 : "FATİH ÜNİVERSİTESİ",
    11 : ["BAŞKENT ÜNİVERSİTESİ","Başkent Üniversitesi"],
    12 : ["ÇAĞ ÜNİVERSİTESİ","Çağ Üniversitesi"],
    13 : ["İZMİR ÜNİVERSİTESİ","İzmir Üniversitesi"],
    14 : ["ZİRVE ÜNİVERSİTESİ","Zirve Üniversitesi"],
    15 : ["YAŞAR ÜNİVERSİTESİ","Yaşar Üniversitesi"],
    16 : ["İSTANBUL AREL ÜNİVERSİTESİ","İstanbul Arel Üniversitesi"],
    17 : ["YENİ YÜZYIL ÜNİVERSİTESİ","Yeni Yüzyıl Üniversitesi","İSTANBUL YENİ YÜZYIL ÜNİVERSİTESİ"],
    18 : ["İSTANBUL BİLGİ ÜNİVERSİTESİ","İstanbul Bilgi Üniversitesi"],
    19 : ["İSTANBUL GELİŞİM ÜNİVERSİTESİ","İstanbul Gelişim Üniversitesi"],
    20 : ["İZMİR EKONOMİ ÜNİVERSİTESİ","İzmir Ekonomi Üniversitesi"],
    21 : ["BEYKENT ÜNİVERSİTESİ","Beykent Üniversitesi"],
    22 : ["AVRASYA ÜNİVERSİTESİ","Avrasya Üniversitesi"],
    23 : ["OKAN ÜNİVERSİTESİ","Okan Üniversitesi","İstanbul Okan Üniversitesi","İSTANBUL OKAN ÜNİVERSİTESİ"],
    24 : ["KOÇ ÜNİVERSİTESİ","Koç Üniversitesi"],
    25 : ["HALİÇ ÜNİVERSİTESİ","Haliç Üniversitesi"],
    26 : ["IŞIK ÜNİVERSİTESİ","Işık Üniversitesi"],
    27 : "ATILIM ÜNİVERSİTESİ",
    28 : ["NİŞANTAŞI ÜNİVERSİTESİ","Nişantaşı Üniversitesi"],
    29 : ["İSTANBUL AYDIN ÜNİVERSİTESİ","İstanbul Aydın Üniversitesi"],
    30 : ["UFUK ÜNİVERSİTESİ","Ufuk Üniversitesi"],
    31 : ["SABANCI ÜNİVERSİTESİ","Sabancı Üniversitesi"],
    32 : ["İSTANBUL 29 MAYIS ÜNİVERSİTESİ","İstanbul 29 Mayıs Üniversitesi"],
    33 : ["MALTEPE ÜNİVERSİTESİ","Maltepe Üniversitesi"],
    34 : ["ULUSLARARASI ANTALYA ÜNİVERSİTESİ","Uluslararası Antalya Üniversitesi"],
    35 : ["TOBB EKONOMİ VE TEKNOLOJİ","TOBB Ekonomi ve Teknoloji Üniversitesi","TOBB EKONOMİ VE TEKNOLOJİ ÜNİVERSİTESİ"],
    36 : ["KTO KARATAY ÜNİVERSİTESİ","KTO Karatay Üniversitesi"],
    37 : ["ÇANKAYA ÜNİVERSİTESİ","Çankaya Üniversitesi"],
    38 : ["İSTANBUL KÜLTÜR ÜNİVERSİTESİ","İstanbul Kültür Üniversitesi"],
    39 : ["YEDİTEPE ÜNİVERSİTESİ","Yeditepe Üniversitesi"],
    40 : ["GİRNE AMERİKAN ÜNİVERSİTESİ","Girne Amerikan Üniversitesi"],
    41 : ["HASAN KALYONCU ÜNİVERSİTESİ","Hasan Kalyoncu Üniversitesi"],
    42 : ["ÜSKÜDAR ÜNİVERSİTESİ","Üsküdar Üniversitesi"],
    43 : ["MELİKŞAH ÜNİVERSİTESİ","Melikşah Üniversitesi"],
    44 : ["CANİK BAŞARI ÜNİVERSİTESİ","Canik Başarı Üniversitesi"],
    45 : ["KADİR HAS ÜNİVERSİTESİ","Kadir Has Üniversitesi"],
    46 : ["İSTANBUL ESENYURT ÜNİVERSİTESİ","İstanbul Esenyurt Üniversitesi"],
    47 : ["İSTANBUL KAVRAM MESLEK","İstanbul Kavram Meslek Yüksekokulu"],
    48 : ["İSTANBUL KEMERBURGAZ ÜNİVERSİTESİ","İstanbul Kemerburgaz Üniversitesi"],
    49 : ["YAKIN DOĞU ÜNİVERSİTESİ","Yakın Doğu Üniversitesi"],
    50 : ["GEDİZ ÜNİVERSİTESİ","Gediz Üniversitesi"],
    51 : ["GEDİK ÜNİVERSİTESİ","Gedik Üniversitesi","İSTANBUL GEDİK ÜNİVERSİTESİ","İstanbul Gedik Üniversitesi"],
    52 : ["İSTANBUL BİLİM ÜNİVERSİTESİ","İstanbul Bilim Üniversitesi"],
    53 : ["ŞİFA ÜNİVERSİTESİ","Şifa Üniversitesi"],
    54 : ["ÖZYEĞİN ÜNİVERSİTESİ","Özyeğin Üniversitesi"],
    55 : ["TOROS ÜNİVERSİTESİ","Toros Üniversitesi"],
    56 : "PİRİ REİS ÜNİVERSİTESİ",
    57 : ["DOĞU AKDENİZ ÜNİVERSİTESİ","Doğu Akdeniz Üniversitesi"],
    58 : ["ULUDAĞ ÜNİVERSİTESİ","BURSA ULUDAĞ ÜNİVERSİTESİ","Bursa Uludağ Üniversitesi","Uludağ Üniversitesi"],
    59 : ["BURSA ORHANGAZİ ÜNİVERSİTESİ","Bursa Orhangazi Üniversitesi"],
    60 : ["GİRESUN ÜNİVERSİTESİ","Giresun Üniversitesi"],
    61 : ["DOĞUŞ ÜNİVERSİTESİ","Doğuş Üniversitesi"],
    62 : "BEYKOZ LOJİSTİK MESLEK",
    63 : ["TÜRK HAVA KURUMU ÜNİVERSİTESİ","Türk Hava Kurumu Üniversitesi"],
    64 : ["HACETTEPE ÜNİVERSİTESİ","Hacettepe Üniversitesi"],
    65 : ["İSTANBUL SABAHATTİN ZAİM","İstanbul Sabahattin Zaim Üniversitesi","İSTANBUL SABAHATTİN ZAİM ÜNİVERSİTESİ"],
    66 : ["BOĞAZİÇİ ÜNİVERSİTESİ","Boğaziçi Üniversitesi"],
    67 : ["MEVLANA ÜNİVERSİTESİ","Mevlana Üniversitesi"],
    68 : ["OSMANİYE KORKUT ATA ÜNİVERSİTESİ","Osmaniye Korkut Ata Üniversitesi"],
    69 : ["LEFKE AVRUPA ÜNİVERSİTESİ","Lefke Avrupa Üniversitesi"],
    70 : ["ORTA DOĞU TEKNİK ÜNİVERSİTESİ","Orta Doğu Teknik Üniversitesi"],
    71 : ["AMASYA ÜNİVERSİTESİ","Amasya Üniversitesi"],
    72 : ["KOCAELİ ÜNİVERSİTESİ","Kocaeli Üniversitesi"],
    73 : ["FIRAT ÜNİVERSİTESİ","Fırat Üniversitesi"],
    74 : ["ACIBADEM ÜNİVERSİTESİ","Acıbadem Üniversitesi","ACIBADEM MEHMET ALİ AYDINLAR ÜNİVERSİTESİ"],
    75 : ["SÜLEYMAN ŞAH ÜNİVERSİTESİ","Süleyman Şah Üniversitesi"],
    76 : ["MEF ÜNİVERSİTESİ","MEF Üniversitesi"],
    77 : ["PLATO MESLEK YÜKSEKOKULU","Plato Meslek Yüksekokulu"],
    78 : ["ANADOLU ÜNİVERSİTESİ","Anadolu Üniversitesi"],
    79 : ["İPEK ÜNİVERSİTESİ","İpek Üniversitesi"],
    80 : ["ABANT İZZET BAYSAL ÜNİVERSİTESİ","Abant İzzet Baysal Üniversitesi","Bolu Abant İzzet Baysal Üniversitesi","BOLU ABANT İZZET BAYSAL ÜNİVERSİTESİ"],
    81 : ["İSTANBUL ÜNİVERSİTESİ","İstanbul Üniversitesi"],
    82 : ["ALANYA HAMDULLAH EMİN PAŞA","ALANYA HAMDULLAH EMİN PAŞA ÜNİVERSİTESİ"],
    83 : ["BEZM-İ ALEM VAKIF ÜNİVERSİTESİ","Bezmialem Vakıf Üniversitesi","BEZM-İ ÂLEM VAKIF ÜNİVERSİTESİ","Bezmiâlem Üniversitesi"],
    84 : ["RECEP TAYYİP ERDOĞAN ÜNİVERSİTESİ","Recep Tayyip Erdoğan Üniversitesi"],
    85 : ["ÇUKUROVA ÜNİVERSİTESİ","Çukurova Üniversitesi"],
    86 : ["BALIKESİR ÜNİVERSİTESİ","Balıkesir Üniversitesi"],
    87 : ["Atılım Üniversitesi"],
    88 : ["Fatih Üniversitesi"],
    89 : ["İstanbul Teknik Üniversitesi","İSTANBUL TEKNİK ÜNİVERSİTESİ"],
    90 : ["TED Üniversitesi","TED ÜNİVERSİTESİ","TED Üniversitesi"],
    91 : ["Mersin Üniversitesi","MERSİN ÜNİVERSİTESİ"],
    92 : ["Biruni Üniversitesi","BİRUNİ ÜNİVERSİTESİ"],
    93 : ["KAFKAS ÜNİVERSİTESİ","Kafkas Üniversitesi"],
    94 : ["AĞRI İBRAHİM ÇEÇEN ÜNİVERSİTESİ","Ağrı İbrahim Çeçen Üniversitesi"],
    95 : ["YILDIRIM BEYAZIT ÜNİVERSİTESİ","Ankara Yıldırım Beyazıt Üniversitesi","ANKARA YILDIRIM BEYAZIT ÜNİVERSİTESİ","Yıldırım Beyazıt Üniversitesi"],
    96 : ["ANKARA ÜNİVERSİTESİ","Ankara Üniversitesi"],
    97 : ["GAZİ ÜNİVERSİTESİ","Gazi Üniversitesi"],
    98 : ["MARMARA ÜNİVERSİTESİ","Marmara Üniversitesi"],
    99 : ["ÇANAKKALE ONSEKİZ MART","Çanakkale Onsekiz Mart Üniversitesi","ÇANAKKALE ONSEKİZ MART ÜNİVERSİTESİ"],
    100 : ["SAKARYA ÜNİVERSİTESİ","Sakarya Üniversitesi"],
    101 : ["SÜLEYMAN DEMİREL ÜNİVERSİTESİ","Süleyman Demirel Üniversitesi"],
    102 : ["DUMLUPINAR ÜNİVERSİTESİ","Kütahya Dumlupınar Üniversitesi","KÜTAHYA DUMLUPINAR ÜNİVERSİTESİ","Dumlupınar Üniversitesi"],
    103 : ["KIRKLARELİ ÜNİVERSİTESİ","Kırklareli Üniversitesi"],
    104 : ["BAYBURT ÜNİVERSİTESİ","Bayburt Üniversitesi"],
    105 : ["ONDOKUZ MAYIS ÜNİVERSİTESİ","Ondokuz Mayıs Üniversitesi"],
    106 : ["BÜLENT ECEVİT ÜNİVERSİTESİ","Zonguldak Bülent Ecevit Üniversitesi","ZONGULDAK BÜLENT ECEVİT ÜNİVERSİTESİ","Bülent Ecevit Üniversitesi","Zonguldak Bülent Ecevit Üniversitesi"],
    107 : ["GAZİOSMANPAŞA ÜNİVERSİTESİ","Gaziosmanpaşa Üniversitesi","Tokat Gaziosmanpaşa Üniversitesi","TOKAT GAZİOSMANPAŞA ÜNİVERSİTESİ"],
    108 : ["KARADENİZ TEKNİK ÜNİVERSİTESİ","Karadeniz Teknik Üniversitesi"],
    109 : ["Diğer"],
    110 : ["NAMIK KEMAL ÜNİVERSİTESİ","Tekirdağ Namık Kemal Üniversitesi","TEKİRDAĞ NAMIK KEMAL ÜNİVERSİTESİ","Namık Kemal Üniversitesi"],
    111 : ["ÇANKIRI KARATEKİN ÜNİVERSİTESİ","Çankırı Karatekin Üniversitesi"],
    112 : ["KARABÜK ÜNİVERSİTESİ","Karabük Üniversitesi"],
    113 : ["MEHMET AKİF ERSOY ÜNİVERSİTESİ","Mehmet Akif Ersoy Üniversitesi","BURDUR MEHMET AKİF ERSOY ÜNİVERSİTESİ","Burdur Mehmet Akif Ersoy Üniversitesi"],
    114 : ["ERZİNCAN ÜNİVERSİTESİ","Erzincan Üniversitesi"],
    115 : ["SİİRT ÜNİVERSİTESİ","Siirt Üniversitesi"],
    116 : ["TÜRK-ALMAN ÜNİVERSİTESİ","Türk-Alman Üniversitesi"],
    117 : ["TRAKYA ÜNİVERSİTESİ","Trakya Üniversitesi"],
    118 : ["NECMETTİN ERBAKAN ÜNİVERSİTESİ","Necmettin Erbakan Üniversitesi","KONYA NECMETTİN ERBAKAN ÜNİVERSİTESİ","Konya Necmettin Erbakan Üniversitesi","NECMETTİN ERBAKAN ÜNİVERSİTESİ"],
    119 : ["SİNOP ÜNİVERSİTESİ","Sinop Üniversitesi"],
    120 : ["KASTAMONU ÜNİVERSİTESİ","Kastamonu Üniversitesi"],
    121 : ["YILDIZ TEKNİK ÜNİVERSİTESİ","Yıldız Teknik Üniversitesi"],
    122 : ["ATATÜRK ÜNİVERSİTESİ","Atatürk Üniversitesi"],
    123 : ["ADNAN MENDERES ÜNİVERSİTESİ","AYDIN ADNAN MENDERES","Adnan Menderes Üniversitesi","Aydın Adnan Menderes Üniversitesi"],
    124 : ["İZMİR KATİP ÇELEBİ ÜNİVERSİTESİ","İzmir Katip Çelebi Üniversitesi","İzmir Kâtip Çelebi Üniversitesi"],
    125 : ["CELAL BAYAR ÜNİVERSİTESİ","Celal Bayar Üniversitesi","Manisa Celal Bayar Üniversitesi"],
    126 : ["UŞAK ÜNİVERSİTESİ","Uşak Üniversitesi"],
    127 : ["MUĞLA SITKI KOÇMAN ÜNİVERSİTESİ","Muğla Sıtkı Koçman Üniversitesi"],
    128 : ["ERCİYES ÜNİVERSİTESİ","Erciyes Üniversitesi"],
    129 : ["Akdeniz Üniversitesi","AKDENİZ ÜNİVERSİTESİ"],
    130 : ["GAZİANTEP ÜNİVERSİTESİ","Gaziantep Üniversitesi"],
    131 : ["MUSTAFA KEMAL ÜNİVERSİTESİ","HATAY MUSTAFA KEMAL ÜNİVERSİTESİ","Mustafa Kemal Üniversitesi","Hatay Mustafa Kemal Üniversitesi"],
    132 : ["YÜZÜNCÜ YIL ÜNİVERSİTESİ","Yüzüncü Yıl Üniversitesi","VAN YÜZÜNCÜ YIL ÜNİVERSİTESİ","Van Yüzüncü Yıl Üniversitesi"],
    133 : ["ESKİŞEHİR OSMANGAZİ ÜNİVERSİTESİ","Eskişehir Osmangazi Üniversitesi"],
    134 : ["BİNGÖL ÜNİVERSİTESİ","Bingöl Üniversitesi"],
    135 : ["AKSARAY ÜNİVERSİTESİ","Aksaray Üniversitesi"],
    136 : ["EGE ÜNİVERSİTESİ","Ege Üniversitesi"],
    137 : ["KONYA TARIM VE GIDA ÜNİVERSİTESİ","KONYA GIDA VE TARIM ÜNİVERSİTESİ","Konya Tarım ve Gıda Üniversitesi","Konya Gıda ve Tarım Üniversitesi"],
    138 : ["GÜMÜŞHANE ÜNİVERSİTESİ","Gümüşhane Üniversitesi"],
    139 : ["PAMUKKALE ÜNİVERSİTESİ","Pamukkale Üniversitesi"],
    140 : ["ABDULLAH GÜL ÜNİVERSİTESİ","Abdullah Gül Üniversitesi"],
    141 : ["SELÇUK ÜNİVERSİTESİ","Selçuk Üniversitesi"],
    142 : ["GALATASARAY ÜNİVERSİTESİ","Galatasaray Üniversitesi"],
    143 : ["BİLECİK ŞEYH EDEBALİ ÜNİVERSİTESİ","Bilecik Şeyh Edebali Üniversitesi"],
    144 : ["MARDİN ARTUKLU ÜNİVERSİTESİ","Mardin Artuklu Üniversitesi"],
    145 : ["CUMHURİYET ÜNİVERSİTESİ","Cumhuriyet Üniversitesi","SİVAS CUMHURİYET ÜNİVERSİTESİ","Sivas Cumhuriyet Üniversitesi"],
    146 : ["İSTANBUL MEDENİYET ÜNİVERSİTESİ","İstanbul Medeniyet Üniversitesi"],
    147 : ["ADIYAMAN ÜNİVERSİTESİ","Adıyaman Üniversitesi"],
    148 : ["KAHRAMANMARAŞ SÜTÇÜ İMAM","KAHRAMANMARAŞ SÜTÇÜ İMAM ÜNİVERSİTESİ","Kahramanmaraş Sütçü İmam Üniversitesi"],
    149 : ["DOKUZ EYLÜL ÜNİVERSİTESİ","Dokuz Eylül Üniversitesi"],
    150 : ["YALOVA ÜNİVERSİTESİ","Yalova Üniversitesi"],
    151 : ["HARRAN ÜNİVERSİTESİ","Harran Üniversitesi"],
    152 : ["IĞDIR ÜNİVERSİTESİ","Iğdır Üniversitesi"],
    153 : ["MUŞ ALPARSLAN ÜNİVERSİTESİ","Muş Alparslan Üniversitesi"],
    154 : ["BURSA TEKNİK ÜNİVERSİTESİ","Bursa Teknik Üniversitesi"],
    155 : ["GEBZE YÜKSEK TEKNOLOJİ ENSTİTÜSÜ"],
    156 : ["KARAMANOĞLU MEHMETBEY","KARAMANOĞLU MEHMETBEY ÜNİVERSİTESİ","Karamanoğlu Mehmetbey Üniversitesi"],
    157 : ["TUNCELİ ÜNİVERSİTESİ","Tunceli Üniversitesi"],
    158 : ["ŞIRNAK ÜNİVERSİTESİ","Şırnak Üniversitesi"],
    159 : ["NEVŞEHİR HACI BEKTAŞ VELİ","NEVŞEHİR HACI BEKTAŞ VELİ ÜNİVERSİTESİ","Nevşehir Hacı Bektaş Veli Üniversitesi"],
    160 : ["BOZOK ÜNİVERSİTESİ","Bozok Üniversitesi","YOZGAT BOZOK ÜNİVERSİTESİ","Yozgat Bozok Üniversitesi"],
    161 : ["KAPADOKYA MESLEK YÜKSEKOKULU",],
    162 : ["ADANA BİLİM VE TEKNOLOJİ","Adana Bilim ve Teknoloji Üniversitesi","Adana Alparslan Türkeş Bilim ve Teknoloji Üniversitesi","ADANA ALPARSLAN TÜRKEŞ BİLİM VE"],
    163 : ["HİTİT ÜNİVERSİTESİ","Hitit Üniversitesi"],
    164 : ["NİĞDE ÜNİVERSİTESİ","Niğde Üniversitesi"],
    165 : ["MİMAR SİNAN GÜZEL SANATLAR","Mimar Sinan Güzel Sanatlar Üniversitesi","MİMAR SİNAN GÜZEL SANATLAR ÜNİVERSİTESİ"],
    166 : ["İNÖNÜ ÜNİVERSİTESİ","İnönü Üniversitesi"],
    167 : ["BİTLİS EREN ÜNİVERSİTESİ","Bitlis Eren Üniversitesi"],
    168 : ["AFYON KOCATEPE ÜNİVERSİTESİ","Afyon Kocatepe Üniversitesi"],
    169 : ["DÜZCE ÜNİVERSİTESİ","Düzce Üniversitesi"],
    170 : ["BARTIN ÜNİVERSİTESİ","Bartın Üniversitesi"],
    171 : ["KIRIKKALE ÜNİVERSİTESİ","Kırıkkale Üniversitesi"],
    172 : ["ERZİNCAN BİNALİ YILDIRIM ÜNİVERSİTESİ","Erzincan Binali Yıldırım Üniversitesi"],
    173 : ["ALTINBAŞ ÜNİVERSİTESİ","Altınbaş Üniversitesi"],
    174 : ["İZMİR YÜKSEK TEKNOLOJİ ENSTİTÜSÜ","İzmir Yüksek Teknoloji Enstitüsü"],
    175 : ["FENERBAHÇE ÜNİVERSİTESİ","Fenerbahçe Üniversitesi"],
    176 : ["SAĞLIK BİLİMLERİ ÜNİVERSİTESİ","Sağlık Bilimleri Üniversitesi"],
    177 : ["İSTANBUL AYVANSARAY ÜNİVERSİTESİ"],
    178 : ["İSTİNYE ÜNİVERSİTESİ","İstinye Üniversitesi"],
    179 : ["İSTANBUL ÜNİVERSİTESİ-","İstanbul Üniversitesi-Cerrahpaşa"],
    180 : ["İZMİR KAVRAM MESLEK ÜNİVERSİTESİ","İzmir Kavram Meslek Yüksekokulu"],
    181 : ["DEMİROĞLU BİLİM ÜNİVERSİTESİ","Demiroğlu Bilim Üniversitesi"],
    182 : ["İSTANBUL RUMELİ ÜNİVERSİTESİ","İstanbul Rumeli Üniversitesi"],
    183 : ["BEYKOZ ÜNİVERSİTESİ","Beykoz Üniversitesi"],
    184 : ["İBN HALDUN ÜNİVERSİTESİ","İbn Haldun Üniversitesi"],
    185 : ["KAPADOKYA ÜNİVERSİTESİ","Kapadokya Üniversitesi"],
    186 : ["İZMİR DEMOKRASİ ÜNİVERSİTESİ","İzmir Demokrasi Üniversitesi"],
    187 : ["NİĞDE ÖMER HALİSDEMİR","Niğde Ömer Halisdemir Üniversitesi"],
    188 : ["İSTANBUL KENT ÜNİVERSİTESİ","İstanbul Kent Üniversitesi","İstanbul Kent Üniversitesi"],
    189 : ["ESKİŞEHİR TEKNİK ÜNİVERSİTESİ","Eskişehir Teknik Üniversitesi"],
    190 : ["KOCAELİ SAĞLIK VE TEKNOLOJİ ÜNİVERSİTESİ","Kocaeli Sağlık ve Teknoloji Üniversitesi"],
    191 : ["KIRŞEHİR AHİ EVRAN ÜNİVERSİTESİ","Kırşehir Ahi Evran Üniversitesi","AHİ EVRAN ÜNİVERSİTESİ","Ahi Evran Üniversitesi"],
    192 : ["ANKARA MEDİPOL ÜNİVERSİTESİ","Ankara Medipol Üniversitesi"],
    193 : ["OSTİM TEKNİK ÜNİVERSİTESİ","Ostim Teknik Üniversitesi"],
    194 : ["MUNZUR ÜNİVERSİTESİ","Munzur Üniversitesi"],
    195 : ["KİLİS 7 ARALIK ÜNİVERSİTESİ","Kilis 7 Aralık Üniversitesi"],
    196 : ["ANKARA HACI BAYRAM VELİ ÜNİVERSİTESİ","Ankara Hacı Bayram Veli Üniversitesi"],
    197 : ["BATMAN ÜNİVERSİTESİ","Batman Üniversitesi"],
    198 : ["TRABZON ÜNİVERSİTESİ","Trabzon Üniversitesi"],
    199 : ["ANKARA SOSYAL BİLİMLER ÜNİVERSİTESİ","ANKARA SOSYAL BİLİMLER","Ankara Sosyal Bilimler Üniversitesi","Ankara Sosyal Bilimler Üniversitesi","Ankara Sosyal Bilimler Üniversitesi Kuzey Kıbrıs Kampüsü"],
    200 : ["ISPARTA UYGULAMALI BİLİMLER ÜNİVERSİTESİ","Isparta Uygulamalı Bilimler Üniversitesi"],
    201 : ["MANİSA CELÂL BAYAR ÜNİVERSİTESİ",],
    202 : ["İSTANBUL SAĞLIK VE TEKNOLOJİ ÜNİVERSİTESİ","İstanbul Sağlık ve Teknoloji Üniversitesi"],
    203 : ["İSTANBUL ŞİŞLİ MESLEK ÜNİVERSİTESİ","İSTANBUL ŞİŞLİ MESLEK YÜKSEKOKULU"],
    204 : ["ANTALYA AKEV ÜNİVERSİTESİ","Antalya Akev Üniversitesi"],
    205 : ["KÜTAHYA SAĞLIK BİLİMLERİ ÜNİVERSİTESİ","Kütahya Sağlık Bilimleri Üniversitesi"],
    206 : ["ALANYA ALAADDİN KEYKUBAT ÜNİVERSİTESİ","Alanya Alaaddin Keykubat Üniversitesi"],
    207 : ["AFYONKARAHİSAR SAĞLIK BİLİMLERİ ÜNİVERSİTESİ","Afyonkarahisar Sağlık Bilimleri Üniversitesi"],
    208 : ["BANDIRMA ONYEDİ EYLÜL ÜNİVERSİTESİ","Bandırma Onyedi Eylül Üniversitesi"],
    209 : ["İSKENDERUN TEKNİK ÜNİVERSİTESİ","İskenderun Teknik Üniversitesi"],
    210 : ["FARUK SARAÇ TASARIM MESLEK YÜKSEKOKULU (İSTANBUL)","FARUK SARAÇ TASARIM MESLEK",],
    211 : ["ARDAHAN ÜNİVERSİTESİ","Ardahan Üniversitesi"],
    212 : ["İSTANBUL GALATA ÜNİVERSİTESİ","İstanbul Galata Üniversitesi"],
    213 : ["GEBZE TEKNİK ÜNİVERSİTESİ","Gebze Teknik Üniversitesi"],
    214 : ["SANKO ÜNİVERSİTESİ","Sanko Üniversitesi"],
    215 : ["İSTANBUL ATLAS ÜNİVERSİTESİ","İstanbul Atlas Üniversitesi"],
    216 : ["HAKKARİ ÜNİVERSİTESİ"],
    217 : ["LOKMAN HEKİM ÜNİVERSİTESİ","Lokman Hekim Üniversitesi"],
    218 : ["ANTALYA BİLİM ÜNİVERSİTESİ","Antalya Bilim Üniversitesi"],
    219 : ["ANKARA BİLİM ÜNİVERSİTESİ","Ankara Bilim Üniversitesi"],
    220 : ["İZMİR BAKIRÇAY ÜNİVERSİTESİ","İzmir Bakırçay Üniversitesi"],
    221 : ["KONYA TEKNİK ÜNİVERSİTESİ","Konya Teknik Üniversitesi"],
    222 : ["YÜKSEK İHTİSAS ÜNİVERSİTESİ","Yüksek İhtisas Üniversitesi"],
    223 : ["SAMSUN ÜNİVERSİTESİ","Samsun Üniversitesi"],
    224 : ["İZMİR TINAZTEPE ÜNİVERSİTESİ","İzmir Tınaztepe Üniversitesi"],
    225 : ["SELAHADDİN EYYUBİ ÜNİVERSİTESİ","Selahaddin Eyyubi Üniversitesi"],
    226 : ["AVRUPA MESLEK YÜKSEKOKULU"],
    227 : ["ERZURUM TEKNİK ÜNİVERSİTESİ","Erzurum Teknik Üniversitesi"],
    228 : ["SAKARYA UYGULAMALI BİLİMLER ÜNİVERSİTESİ","Sakarya Uygulamalı Bilimler Üniversitesi"],
    229 : ["AKDENİZ KARPAZ ÜNİVERSİTESİ"],
    230 : ["KIRGIZİSTAN-TÜRKİYE MANAS"],
    231 : ["ORDU ÜNİVERSİTESİ","Ordu Üniversitesi"],
    232 : ["HOCA AHMET YESEVİ TÜRK-KAZAK"],
    233 : ["POLİS AKADEMİSİ"],
    234 : ["Dicle Üniversitesi"],
    235 : ["HARP AKADEMİLERİ (KARA, DENİZ,"],
    236 : ["KAYSERİ ÜNİVERSİTESİ","Kayseri Üniversitesi"],
    237 : ["TARSUS ÜNİVERSİTESİ","Tarsus Üniversitesi"],
    238 : ["KAHRAMANMARAŞ İSTİKLAL ÜNİVERSİTESİ","Kahramanmaraş İstiklal Üniversitesi"],
    239 : ["ANKARA MÜZİK VE GÜZEL SANATLAR ÜNİVERSİTESİ"],
    240 : ["GAZİANTEP İSLAM BİLİM VE TEKNOLOJİ ÜNİVERSİTESİ"],
    241 : ["Brown University"],
    242 : ["University of Southern California"],
    243 : ["Gaziantep İslam Bilim ve Teknoloji Üniversitesi"],
    244 : ["Bard College"],
    245 : ["Uluslararası Final Üniversitesi"],
    246 : ["Artvin Çoruh Üniversitesi","ARTVİN ÇORUH ÜNİVERSİTESİ"],
    247 : ["İstanbul Topkapı Üniversitesi"],
    248 : ["Jandarma ve Sahil Güvenlik Akademisi(Askeri)"],
    249 : ["Milli Savunma Üniversitesi (Askerî)"],
    250 : ["Hakkari Üniversitesi"],
    251 : ["Piri Reis Üniversitesi"],
    252 : ["DİCLE ÜNİVERSİTESİ"],
}

universite_adlari_duzgun = {uni: num for num, unis in universite_adlari.items() for uni in (unis if isinstance(unis, list) else [unis])}

not_ortalamasi = {
    '3.50 - 4.00' : 5,
    '3.00 - 3.49' : 4,
    '2.50 - 2.99' : 3,
    '1.80 - 2.49' : 2,
    'Hazırlığım' : 0,
    '0 - 1.79': 1,
}

cinsiyet = {
    'Kadın' : 1,
    'Erkek' : 2,
    'ERKEK' : 2,
    'Belirtmek istemiyorum' : 0
}

universite_turu = {
    'Devlet' : 1,
    'DEVLET' : 1,
    'Özel' : 2,
    'ÖZEL' : 2,
}

burs = {
    'Evet' : 1,
    'Hayır' : 0,
    'hayır' : 0,
    'evet' : 1,
    'EVET' : 1,
}

sinif = {
    '1' : 1,
    '2' : 2,
    '3' : 3,
    '4' : 4,
    '5' : 5,
    '6' : 6,
    'Hazırlık' : 0,
}

daha_once_uni = {
    'Hayır' : 0,
    'Evet' : 1,
}

baska_burs = {
    'Hayır' : 0,
    'Evet' : 1,
}

anne_calisma = {
    'Hayır' : 0,
    'Evet' : 1,
}

baba_calisma = {
    'Hayır' : 0,
    'Evet' : 1,
}

girisimcilik_kulup = {
    'Evet' : 1,
    'Hayır' : 0,
}

spor = {
    'Evet' : 1,
    'Hayır' : 0,
}

stk_uye = {
    'Evet' : 1,
    'Hayır' : 0,
}

stk_proje = {
    'Evet' : 1,
    'Hayır' : 0,
}

girisimcilik_deneyim = {
    'Evet' : 1,
    'Hayır' : 0,
}

ingilizce_bilme = {
    'Evet' : 1,
    'Hayır' : 0,
}

# Use the mappings to convert the test data and fill the missing values
df['Baba Sektor'] = df['Baba Sektor'].map(sektor_mapping)
df['Anne Sektor'] = df['Anne Sektor'].map(sektor_mapping)
df['Lise Turu'] = df['Lise Turu'].map(lisetip)
df['Anne Egitim Durumu'] = df['Anne Egitim Durumu'].map(egitim_mapping)
df['Baba Egitim Durumu'] = df['Baba Egitim Durumu'].map(egitim_mapping)
df['Lise Bolumu'] = df['Lise Bolumu'].map(lise_bolumu_mapping)
df['Bölüm'] = df['Bölüm'].map(bolum_mapping)
df['Universite Adi'] = df['Universite Adi'].map(universite_adlari_duzgun)
df['Universite Not Ortalamasi'] = df['Universite Not Ortalamasi'].map(not_ortalamasi)
df['Universite Not Ortalamasi'] = df['Universite Not Ortalamasi'].fillna(0)
df["Cinsiyet"] = df["Cinsiyet"].map(cinsiyet)
df['Cinsiyet'] = df['Cinsiyet'].fillna(0)
df['Universite Turu'] = df['Universite Turu'].map(universite_turu)
df['Universite Turu'] = df['Universite Turu'].fillna(0)
df['Burs Aliyor mu?'] = df["Burs Aliyor mu?"].map(burs)
df['Burs Aliyor mu?'] = df['Burs Aliyor mu?'].fillna(0)
df["Universite Kacinci Sinif"] = df["Universite Kacinci Sinif"].map(sinif)
df["Universite Kacinci Sinif"] = df["Universite Kacinci Sinif"].fillna(0)
df["Daha Once Baska Bir Universiteden Mezun Olmus"] = df["Daha Once Baska Bir Universiteden Mezun Olmus"].map(daha_once_uni)
df["Daha Once Baska Bir Universiteden Mezun Olmus"] = df["Daha Once Baska Bir Universiteden Mezun Olmus"].fillna(0)
df["Baska Bir Kurumdan Burs Aliyor mu?"] = df["Baska Bir Kurumdan Burs Aliyor mu?"].map(baska_burs)
df["Baska Bir Kurumdan Burs Aliyor mu?"] = df["Baska Bir Kurumdan Burs Aliyor mu?"].fillna(0)
df["Anne Calisma Durumu"] = df["Anne Calisma Durumu"].map(anne_calisma)
df["Anne Calisma Durumu"] = df["Anne Calisma Durumu"].fillna(0)
df["Baba Calisma Durumu"] = df["Baba Calisma Durumu"].map(anne_calisma)
df["Baba Calisma Durumu"] = df["Baba Calisma Durumu"].fillna(0)
df["Girisimcilik Kulupleri Tarzi Bir Kulube Uye misiniz?"] = df["Girisimcilik Kulupleri Tarzi Bir Kulube Uye misiniz?"].map(girisimcilik_kulup)
df["Girisimcilik Kulupleri Tarzi Bir Kulube Uye misiniz?"] = df["Girisimcilik Kulupleri Tarzi Bir Kulube Uye misiniz?"].fillna(0)
df["Profesyonel Bir Spor Daliyla Mesgul musunuz?"] = df["Profesyonel Bir Spor Daliyla Mesgul musunuz?"].map(spor)
df["Profesyonel Bir Spor Daliyla Mesgul musunuz?"] = df["Profesyonel Bir Spor Daliyla Mesgul musunuz?"].fillna(0)
df["Aktif olarak bir STK üyesi misiniz?"] = df["Aktif olarak bir STK üyesi misiniz?"].map(stk_uye)
df["Aktif olarak bir STK üyesi misiniz?"] = df["Aktif olarak bir STK üyesi misiniz?"].fillna(0)
df["Stk Projesine Katildiniz Mi?"] = df["Stk Projesine Katildiniz Mi?"].map(stk_proje)
df["Stk Projesine Katildiniz Mi?"] = df["Stk Projesine Katildiniz Mi?"].fillna(0)
df["Girisimcilikle Ilgili Deneyiminiz Var Mi?"] = df["Girisimcilikle Ilgili Deneyiminiz Var Mi?"].map(girisimcilik_deneyim)
df["Girisimcilikle Ilgili Deneyiminiz Var Mi?"] = df["Girisimcilikle Ilgili Deneyiminiz Var Mi?"].fillna(0)
df['Ingilizce Biliyor musunuz?'] = df['Ingilizce Biliyor musunuz?'].map(ingilizce_bilme)
df['Ingilizce Biliyor musunuz?'] = df['Ingilizce Biliyor musunuz?'].fillna(0)

df.to_csv('filtered_train.csv', index=False)  # Save the filtered data as a new csv file

print("Filtered train data saved as 'filtered_train.csv'") # Gives information about the process completed successfully