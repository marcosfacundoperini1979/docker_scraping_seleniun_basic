# Utiliza la imagen oficial de Python 3.11 como base
FROM python:3.11.6

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos de la aplicación al directorio de trabajo
COPY . .

# Instala Selenium
RUN pip install selenium==4.11.2

# Instala el navegador Chrome y sus dependencias
COPY google-chrome-stable_current_amd64.deb .
RUN apt-get update && apt-get install -y ./google-chrome-stable_current_amd64.deb && apt-get install -f

# Copia el chromedriver al directorio /app
COPY chromedriver .

# CMD ["python", "main.py"]
