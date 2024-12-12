# Sistem Python'ı kullanıldığı için temel imaj belirlemiyoruz

# Çalışma dizinini ayarla
WORKDIR /app

# Proje dosyalarını kopyala
COPY . .

# Gerekli Python paketlerini yükle
RUN pip install --no-cache-dir -r requirements.txt

# Uygulamayı çalıştır
CMD ["python3", "main.py"]