# Rembg API

This project provides a simple Flask-based API for removing backgrounds from images using the `rembg` library. The API takes an image file in a POST request and returns the processed image with the background removed.

## Features

- Remove background from images
- Dockerized for easy deployment
- Simple and easy-to-use API

## Requirements

- Python 3.12
- Docker (optional, for containerized deployment)

## Setup

### Docker Setup

1. **Clone the repository**:
    ```sh
    git clone https://github.com/kenn2799/rembg-api
    cd rembg-api
    ```

2. **Build the Docker image**:
    ```sh
    docker build -t rembg-api .
    ```

3. **Run the Docker container**:
    ```sh
    docker run -d -p 5000:5000 --name rembg-api-container rembg-api
    ```

## API Endpoints

### Remove Background

- **URL**: `/remove-bg`
- **Method**: `POST`
- **Form Data**:
    - `file`: The image file to process
- **Response**: The processed image with the background removed

### Root

- **URL**: `/`
- **Method**: `GET`
- **Response**: A simple message to confirm the API is running
