# Base image olarak Python 3.12 kullanıyoruz
FROM python:3.12-slim

# Çalışma dizinini ayarlayın
WORKDIR /erdem-helloworld

# Gerekli kütüphaneleri yüklemek için requirements.txt dosyasını kopyalayın
COPY requirements.txt .

# Gereksinimleri yükleyin
RUN pip install --no-cache-dir -r requirements.txt

# Uygulama dosyalarınızı kopyalayın
# COPY . . # everything copied
# COPY hello-world.py .

# Flask uygulamanızı çalıştırın
CMD ["python", "hello-world.py"]
