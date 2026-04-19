# Dockerfile
# Containerized setup for running the Tiny VM Desktop Environment

# Use an official Ubuntu as a base image
FROM ubuntu:20.04

# Set the maintainer label
LABEL maintainer="youremail@example.com"

# Set environment variables to avoid interactive prompts during build
ENV DEBIAN_FRONTEND=noninteractive

# Update and install necessary packages
RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y qemu qemu-kvm libvirt-bin python3-pip git curl

# Copy the project files into the container
COPY . /app

# Set the working directory
WORKDIR /app

# Install Python dependencies
RUN pip3 install -r requirements.txt

# Expose any necessary ports (example)
EXPOSE 8080

# Command to run the application
CMD ["python3", "src/main.py"]
