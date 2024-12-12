# Çalışma dizinini ayarla
WORKDIR /app

# Proje dosyalarını kopyala
COPY . .

# Gerekli bağımlılıkları yükle
RUN pip install --no-cache-dir -r requirements.txt

# Etkileşimli terminal açılması için bir komut belirtme
CMD ["/bin/bash"]