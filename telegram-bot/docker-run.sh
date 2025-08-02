#!/bin/bash

# Telegram Bot Docker Management Script

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to print colored output
print_status() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Check if .env file exists
if [ ! -f ".env" ]; then
    print_error ".env file not found!"
    print_status "Please create a .env file with your BOT_TOKEN and REMOVE_BG_API_KEY"
    exit 1
fi

# Function to build the Docker image
build() {
    print_status "Building Docker image..."
    docker build -t telegram-removebg-bot .
    print_success "Docker image built successfully!"
}

# Function to run the container
run() {
    print_status "Starting the bot container..."
    docker run -d \
        --name removebg-bot \
        --restart unless-stopped \
        --env-file .env \
        telegram-removebg-bot
    print_success "Bot container started!"
}

# Function to run with docker-compose
compose_up() {
    print_status "Starting services with docker-compose..."
    docker-compose up -d
    print_success "Services started with docker-compose!"
}

# Function to stop the container
stop() {
    print_status "Stopping the bot..."
    docker stop removebg-bot 2>/dev/null || print_warning "Container not running"
    docker rm removebg-bot 2>/dev/null || print_warning "Container already removed"
    print_success "Bot stopped!"
}

# Function to view logs
logs() {
    print_status "Showing bot logs..."
    docker logs -f removebg-bot
}

# Function to show status
status() {
    print_status "Container status:"
    docker ps -a --filter name=removebg-bot
}

# Main script logic
case "${1:-help}" in
    build)
        build
        ;;
    run)
        build
        run
        ;;
    compose)
        compose_up
        ;;
    stop)
        stop
        ;;
    restart)
        stop
        build
        run
        ;;
    logs)
        logs
        ;;
    status)
        status
        ;;
    help|*)
        echo "Telegram Bot Docker Management"
        echo ""
        echo "Usage: $0 {build|run|compose|stop|restart|logs|status|help}"
        echo ""
        echo "Commands:"
        echo "  build    - Build the Docker image"
        echo "  run      - Build and run the bot container"
        echo "  compose  - Start with docker-compose"
        echo "  stop     - Stop and remove the container"
        echo "  restart  - Stop, rebuild, and start the container"
        echo "  logs     - Show container logs"
        echo "  status   - Show container status"
        echo "  help     - Show this help message"
        ;;
esac
