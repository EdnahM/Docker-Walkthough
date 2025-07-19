# English ↔ Swahili Translator

A simple, elegant web application for translating between English and Swahili using OpenAI's GPT API. Built with Flask and designed to be easily dockerized and deployed.

## Features

- 🌍 Bidirectional translation (English ↔ Swahili)
- 🎨 Modern, responsive UI
- 🐳 Docker support
- 🚀 Production-ready with Gunicorn
- 💪 Health checks and error handling
- 📱 Mobile-friendly design

## Prerequisites

- Docker and Docker Compose
- OpenAI API key

## Quick Start

### 1. Clone and Setup

```bash
git clone <your-repo-url>
cd translator-app
```

### 2. Set up environment

```bash
# Copy the example environment file
cp .env.example .env

# Edit .env and add your OpenAI API key
nano .env
```

### 3. Run with Docker Compose

```bash
# Build and run
docker-compose up --build

# Or run in background
docker-compose up -d --build
```

The app will be available at `http://localhost:5000`

## Manual Docker Build

### Build the image

```bash
docker build -t translator-app .
```

### Run the container

```bash
docker run -d \
  --name translator \
  -p 5000:5000 \
  -e OPENAI_API_KEY=your_api_key_here \
  translator-app
```

## Pushing to Docker Hub

### 1. Tag your image

```bash
# Replace 'yourusername' with your Docker Hub username
docker tag translator-app yourusername/translator-app:latest
docker tag translator-app yourusername/translator-app:v1.0
```

### 2. Push to Docker Hub

```bash
# Login to Docker Hub
docker login

# Push the images
docker push yourusername/translator-app:latest
docker push yourusername/translator-app:v1.0
```

### 3. Run from Docker Hub

```bash
docker run -d \
  --name translator \
  -p 5000:5000 \
  -e OPENAI_API_KEY=your_api_key_here \
  yourusername/translator-app:latest
```

## Project Structure

```
translator-app/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── Dockerfile            # Docker configuration
├── docker-compose.yml    # Docker Compose configuration
├── .env.example         # Environment variables template
├── templates/
│   └── index.html       # Frontend template
└── README.md           # This file
```

## API Endpoints

- `GET /` - Main application interface
- `POST /translate` - Translation API endpoint
- `GET /health` - Health check endpoint

### Translation API Usage

```bash
curl -X POST http://localhost:5000/translate \
  -H "Content-Type: application/json" \
  -d '{
    "text": "Hello, how are you?",
    "source_lang": "en",
    "target_lang": "sw"
  }'
```

## Configuration

### Environment Variables

- `OPENAI_API_KEY` - Your OpenAI API key (required)
- `FLASK_ENV` - Flask environment (default: production)

### Customization

You can modify the following in `app.py`:
- Change the OpenAI model (currently using `gpt-3.5-turbo`)
- Adjust max tokens for translation
- Add more language pairs
- Modify translation prompts

## Development

### Local Development

```bash
# Install dependencies
pip install -r requirements.txt

# Set environment variable
export OPENAI_API_KEY=your_api_key_here

# Run the app
python app.py
```

### Adding More Languages

To add more language pairs, modify the `/translate` endpoint in `app.py` and update the frontend accordingly.

## Production Deployment

The Docker image uses Gunicorn for production deployment with:
- 2 worker processes
- 60-second timeout
- Health checks every 30 seconds
- Non-root user for security

## Troubleshooting

### Common Issues

1. **API Key Error**: Make sure your OpenAI API key is valid and has sufficient credits
2. **Port Conflicts**: Change the port mapping in docker-compose.yml if 5000 is occupied
3. **Build Failures**: Ensure Docker has sufficient resources allocated

### Checking Logs

```bash
# Docker Compose logs
docker-compose logs -f

# Container logs
docker logs translator
```

## License

## resources:
https://claude.ai/public/artifacts/2c84c8df-68e8-40ee-9133-3b9c350afd6d

https://docs.docker.com/engine/install/ubuntu/

https://docker-curriculum.com/

``` bash
$ docker login --username=maryatdocker [email protected]
```

```bash
Password:
WARNING: login credentials saved in C:\Users\sven\.docker\config.json
Login Succeeded
```
   
