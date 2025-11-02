FROM python:3.11.14
WORKDIR /usr/app
COPY . .
RUN pip install --no-cache-dir -r requirement.txt
EXPOSE 5000
CMD ["python", "./app.py"]
