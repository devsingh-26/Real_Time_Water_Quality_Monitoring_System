# Real-Time Water Quality Monitoring System

A real-time water quality monitoring system built using:

- Python
- Kafka
- FastAPI
- Docker
- HTML/CSS/JavaScript

## Features

- Real-time sensor simulation
- Kafka event streaming
- AI-based water quality analysis
- Live dashboard monitoring
- FastAPI backend APIs
- Dockerized architecture

---

## Technologies Used

- Python
- Apache Kafka
- FastAPI
- Docker
- HTML/CSS/JavaScript

---

## System Architecture

Producer → Kafka → Consumer → AI Analysis → FastAPI → Dashboard

---

## Parameters Monitored

- Temperature
- pH
- Turbidity
- TDS
- Water Level

---

## How to Run

### 1. Start Docker

```bash
docker compose up --build
```

### 2. Start Consumer

```bash
python consumer.py
```

### 3. Start Producer

```bash
python producer.py
```

### 4. Start FastAPI

```bash
uvicorn app:app --reload
```

---

## Dashboard

Open:

```text
dashboard/index.html
```

---

## API Endpoint

```text
http://127.0.0.1:8000/dashboard
```

---

## Project Output

- SAFE / UNSAFE water analysis
- Real-time monitoring
- Live dashboard updates
