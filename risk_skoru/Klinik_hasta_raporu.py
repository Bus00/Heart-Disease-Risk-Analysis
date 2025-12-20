import pandas as pd

#veri dosyasını okut
df= pd.read_csv("heart_diseasee.csv",sep=";")

#format kontrolü
print("İlk 5 satır:")
print(df.head())

#EDA
print("\nKolonlar:")
print(df.columns)
print("\n")

#Anlamlı isimlere çevirme
df=df.rename(columns={
    "age": "yaş",
    "sex": "cinsiyet",
    "trestbps": "resting_bp",
    "chol": "kolestrol",
    "fbs": "açlık_kan_şekeri",
    "thalach": "max_kalp_atışı",
    "exang": "egzersiz_göğüs_ağrısı",
    "cp": "göğüs_acısı",
    "oldpeak": "oldpeak",
    "ca": "num_vessels",
    "thal":"thal",
    "target": "target"
})

#risk skor hesaplama
def kalp_kriz_risk_hesapla(row):
    score = 0

    # yaş
    if row["yaş"] >= 70:
        score += 4
    elif row["yaş"] >= 60:
        score += 3
    elif row["yaş"] >= 50:
        score += 2
    elif row["yaş"] >= 45:
        score += 1

    # tansiyon
    if row["resting_bp"] >= 160:
        score += 4
    elif row["resting_bp"] >= 150:
        score += 3
    elif row["resting_bp"] >= 140:
        score += 2
    elif row["resting_bp"] >= 130:
        score += 1

    # kolesterol
    if row["kolestrol"] >= 290:
        score += 3
    elif row["kolestrol"] >= 240:
        score += 2
    elif row["kolestrol"] >= 200:
        score += 1

    # açlık kan şekeri
    if row["açlık_kan_şekeri"] == 1:
        score += 1

    # egzersiz göğüs ağrısı
    if row["egzersiz_göğüs_ağrısı"] == 1:
        score += 2

    # ST depresyonu
    if row["oldpeak"] >= 2:
        score += 2
    elif row["oldpeak"] >= 1:
        score += 1

    return score

          
#satır satır hastaya özgü risk skoru üret
df["risk_skoru"]= df.apply(kalp_kriz_risk_hesapla, axis=1) 

def risk_seviyesi(score):
    if score<=3:
        return "Düşük Risk"
    elif score<=8:
        return "Orta Risk"
    else:
        return "Yüksek Risk"
    
df["risk_level"] = df["risk_skoru"].apply(risk_seviyesi)


print("Risk seviyesi dağılımı:")
print(df["risk_level"].value_counts())
print("\n")

print("Gerçek hastalık durumu (target):")
print(df["target"].value_counts())
print("\n")


df.to_csv("heart_disease_risk_score.csv", index=False)
df.to_excel("heart_disease_risk_table.xlsx", index=False)


# Risk seviyesi ile gerçek hastalık durumunun karşılaştırılması
comparison = pd.crosstab(df["risk_level"], df["target"])


print("Analiz tamamlandı.")
print("Sonuç dosyası1: heart_disease_risk_score.xlsx")  
print("Sonuç dosyası2: heart_disease_risk_score.csv")  