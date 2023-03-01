FROM python
COPY . /app
WORKDIR /app

RUN apt update -y && \
    apt install -y python3-pip && \
    pip install --upgrade pip && \
    pip install -r requirements.txt && \
    rm -rf /var/lib/apt/lists/*

CMD ["uvicorn", "src.main:app"]