FROM python:3.11.4-slim-buster

# Update and install awscli
RUN apt update -y && apt install awscli -y

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt && \
    pip install --upgrade accelerate && \
    pip uninstall -y transformers accelerate && \
    pip install transformers accelerate

# Expose the port the app runs on
EXPOSE 8080

# Copy the entrypoint script
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Set the entrypoint
ENTRYPOINT ["/entrypoint.sh"]
