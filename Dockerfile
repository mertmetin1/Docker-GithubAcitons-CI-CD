# Temel Python görüntüsünü kullan
FROM python:3.9-slim

# Çalışma dizinini belirle
WORKDIR /app

# requirements.txt dosyasını kopyala ve bağımlılıkları yükle
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Flask uygulamasını kopyala
COPY app.py .

# PDF dosyasını da konteynere kopyala
COPY yivliinsaat.pdf /app/yivliinsaat.pdf


# Uygulamayı çalıştırmak için komut
CMD ["python", "app.py"]
