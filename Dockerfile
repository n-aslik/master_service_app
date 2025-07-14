FROM python:3.13-slim
WORKDIR /master_service_app
COPY . .
RUN /bin/sh -c pip install --no-cache-dir -r requirements.txt
CMD ["python", "main.py"]