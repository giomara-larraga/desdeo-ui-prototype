FROM python:3.10

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire application code into the container
COPY . .


EXPOSE 8080

# Set the default command to run the application
CMD ["gunicorn", "-b", "0.0.0.0:8080", "app:server"]









