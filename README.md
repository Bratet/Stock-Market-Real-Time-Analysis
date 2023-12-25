# Stock Market Real-Time Analysis

## Introduction

Welcome to the Stock Market Real-Time Analysis project! This tool provides a dynamic way to analyze and visualize stock market data in real time.

## Getting Started

### Prerequisites

Before you begin, ensure you have Docker installed on your system. If you don't have Docker, you can download it from [Docker&#39;s official website](https://www.docker.com/get-started).

### Installation

To install and run the project, follow these steps:

1. Clone the repository to your local machine.

   ```bash
   git clone https://github.com/Bratet/Stock-Market-Real-Time-Analysis.git
   ```

2. Navigate to the project directory.

   ```bash
   cd Stock-Market-Real-Time-Analysis
   ```

3. Build and run the Docker container:

   ```bash
   docker-compose up --build
   ```

### Data processing

If you plan on re-training your own model on our dataset, run the `notebooks/data_processing.py` notebook, this should result in the creatio of a `data.csv` file inside the `data/`folder that you can use for your own model.

## Usage

Once the Docker container is up and running, execute the `main.py` script to start the application:

```bash
python src/main.py
```

This will initiate the real-time analysis of the stock market data.
