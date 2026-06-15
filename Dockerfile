# Use the same base image as specified in docker-compose.yml
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the server script and other application files to the container
COPY tcp-server.py .
# If client or other files are needed, they are copied or omitted based on build context.
# Since it is a server, copying tcp-server.py is the primary requirement.
# Let's copy everything in the directory except what is gitignored/dockerignored.
COPY . .

# Expose the port the server listens on
EXPOSE 9999

# Run the python script with unbuffered output (-u)
CMD ["python", "-u", "tcp-server.py"]
