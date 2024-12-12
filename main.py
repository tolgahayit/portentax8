# Gerekli kütüphaneleri yükleme
import numpy as np
from tensorflow.keras.models import load_model

# Modeli yükle
model = load_model('./model/C_12leads_EF_resnet_92.h5')

# EKG verisini yükle
ekg_data = np.load('./sample_ecgs/500Hz_RURAL_109270_20230830121417.npy')

# Şekli kontrol et
print("EKG Verisi Şekli (Orijinal):", ekg_data.shape)

# İlk boyutu sıkıştır ve transpoze et (5000, 12) olacak şekilde
ekg_data = np.squeeze(ekg_data, axis=0).T
print("Transpoze Sonrası Şekil:", ekg_data.shape)

# Çift indeksli örnekleri seç (0, 2, 4, ...)
ekg_data_even_indices = ekg_data[::2, :]  # (2500, 12)

# Model giriş boyutuna uygun hale getir
ekg_data_even_indices = np.expand_dims(ekg_data_even_indices, axis=0)  # (1, 2500, 12)
print("Model Girişi Şekli:", ekg_data_even_indices.shape)

# Modelden tahmin alma
predictions = model.predict(ekg_data_even_indices)

# Sonuçları yazdırma
print("Tahmin Sonuçları:", predictions)