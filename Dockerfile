FROM ubuntu:24.04

WORKDIR /app

COPY . .

RUN apt update && \
    apt install -y python3 python3-pip && \
    apt install -y python3-dev default-libmysqlclient-dev build-essential && \
    apt install -y pkg-config && \
    pip install --break-system-packages --no-cache-dir -r requirements.txt

RUN chmod +x startup.sh
EXPOSE 8000

CMD ["./startup.sh"]