FROM python:3
WORKDIR /app
COPY src/dog.py .
COPY src/test_dog.py .
CMD ["python", "-m", "unittest", "/app/test_dog.py"]