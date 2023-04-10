# FROM python:3.9-slim
FROM alpine:latest

RUN apk update && \
    apk add nmap exiftool sed gawk grep python3 py3-pip && \
    # ln -s /usr/bin/python3 /usr/bin/python && \
    pip install openpyxl

RUN pip install flask

COPY . /app
COPY ./templates /app
COPY ./code /app
WORKDIR app
RUN chmod +x file_import.sh 
RUN chmod +x file_metadata.sh


CMD ["python", "app.py"] 


# FROM alpine:latest

# RUN apk update && \
#     apk add nmap exiftool sed gawk grep python3 py3-pip && \
#     ln -s /usr/bin/python3 /usr/bin/python && \
#     pip install openpyxl

# WORKDIR /app

# COPY code_import.sh .

# VOLUME /app

# CMD ["sh", "code_import.sh"]
