FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt ./requirements.txt
RUN apt-get update && apt-get install -y python3-opencv
RUN pip install opencv-python
RUN pip install -r requirements.txt
EXPOSE 8501
COPY . /app
ENTRYPOINT ["streamlit", "run"]

CMD ["main.py"]
