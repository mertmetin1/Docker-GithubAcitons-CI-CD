# Temel Python görüntüsünü kullan
FROM python:3.9-slim

# Çalışma dizinini belirle
WORKDIR /app

# requirements.txt dosyasını kopyala ve bağımlılıkları yükle
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Flask uygulamasını kopyala
COPY app.py .

# Uygulamayı çalıştırmak için komut
CMD ["python", "app.py"]
