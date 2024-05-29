FROM python:3.12

# Set a working directory
WORKDIR /app

# Copy all the files in the container
COPY . .

# Install dependices
RUN pip install -r requirements.txt


EXPOSE 5001

ENV FLASK_ENV=devlopment
ENV GOOGLE_API_KEY=${GOOGLE_API_KEY}


CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]