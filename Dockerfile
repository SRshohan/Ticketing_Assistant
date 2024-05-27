FROM python:3.12

# Set a working directory
WORKDIR /app

# Copy all the files in the container
COPY . .

# Install dependices
RUN pip install -r requirements.txt


EXPOSE 5000

CMD [ "python", "./app.py" ]