
# Kalp Hastalığı Risk Analizi (Heart Disease Risk Analysis)

Bu proje, klinik hasta verileri kullanılarak "kural tabanlı bir risk skoru" oluşturmayı ve hastaların "kalp hastalığı risk seviyelerini" analiz etmeyi amaçlamaktadır.

Proje, veri analizi (EDA), özellik dönüştürme (feature engineering) ve sonuçların tablo halinde dışa aktarılmasını kapsamaktadır.
----------------------------------------------------------------------------------------------------------

# Kullanılan Veri Seti

- Heart Disease Dataset (UCI / Cleveland)
- Hasta demografik bilgileri ve klinik ölçümler içerir
- Hedef değişken (`target`):
  - '1' → Kalp hastalığı var  
  - '0' → Kalp hastalığı yok  
----------------------------------------------------------------------------------------------------------

# Kullanılan Teknolojiler

- Python
- pandas
- NumPy
- CSV / Excel çıktıları

----------------------------------------------------------------------------------------------------------

# Yapılan Analizler

- Veri setinin okunması ve incelenmesi (EDA)
- Anlamlı sütun isimlendirmeleri
- Klinik kurallara dayalı "risk skoru hesaplama"
- Risk seviyelerinin sınıflandırılması:
  - Düşük Risk
  - Orta Risk
  - Yüksek Risk
- Risk seviyesi dağılımlarının incelenmesi
- Sonuçların CSV ve Excel formatında kaydedilmesi

----------------------------------------------------------------------------------------------------------

# Risk Skoru Yaklaşımı

Risk skoru aşağıdaki klinik parametreler kullanılarak hesaplanmıştır:

- Yaş
- Dinlenme tansiyonu (resting blood pressure)
- Kolesterol
- Açlık kan şekeri
- Egzersizle göğüs ağrısı (exercise-induced angina)
- ST segment depresyonu (oldpeak)

Her hasta için bu kriterlere göre bir "toplam risk puanı" hesaplanmış ve risk seviyeleri belirlenmiştir.

----------------------------------------------------------------------------------------------------------

# Çıktı Dosyaları

- `heart_disease_risk_table.csv`  
  → GitHub ve veri paylaşımı için

- `heart_disease_risk_table.xlsx`  
  → Excel üzerinde tablo, filtreleme ve sunum için

> CSV dosyası Excel, Google Sheets veya Numbers ile tablo olarak açılabilir.

----------------------------------------------------------------------------------------------------------

# Çalıştırma kodunun olduğu dosya
python Klinik_hasta_raporu.py
