# Resmi Python Docker imajını kullan
#FROM python:3.9

# Çalışma dizini oluştur
WORKDIR /app

# Gerekli paketleri yükle
RUN pip install numpy

# Konteyner giriş noktası
CMD ["python3"]
