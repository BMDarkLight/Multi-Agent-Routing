# Multi-Agent Question Routing System

## 🔍 Overview

This project builds a containerized FastAPI service that leverages large language models (LLMs) and LangGraph to implement a multi-agent question routing system. Incoming questions are classified and routed to specialized agents (MathBot, CodeBot, TravelBot) which provide targeted responses, enabling efficient and accurate handling of diverse queries through a clean API interface.

## 📦 Tech Stack

- **FastAPI** for the HTTP service  
- **LangGraph** for multi-agent orchestration 
- **Docker & Docker Compose** for containerization  
- **GitHub Codespaces** (`vs code extension`) for development  
- **GitHub Actions** (`.github/workflows/ci.yml`) for CI (lint + tests)  
- **Pytest** for unit testing  

---

## 🔧 Features & Endpoints

### 🤖 Agent Routing

As visualized by the **LangGragh** using **grandalf**

```shell
                        +---------+                             
                        |__start__|                             
                        +---------+                             
                              *                                
                              *                                
                              *                
                        +----------+                           
                       .| classify |.                          
                   .... +----------+ ....                      
               ....      .       ..      ....                  
           ....        ..          .         ....              
        ...           .             .            ...           
+------+        +------+        +--------+        +---------+  
| code |***     | math |        | travel |       *| unknown |  
+------+   **** +------+*       +--------+   **** +---------+  
               ****      *       **      ****                  
                   ****   **    *    ****                      
                       ***  *  *  ***                          
                        +---------+                            
                        | __end__ |                            
                        +---------+                            
```

### 🌐 API Endpoints

| Endpoint    | Method | Description                          |
|-------------|--------|--------------------------------------|
| `/ask`      | POST   | Accepts `{ "question": "..." }`, returns `{ "agent": "...", "answer": "..." }` |
| `/health`   | GET    | Returns service status               |

---

## 🐳 Docker Image

A pre-built Docker image is available on Docker Hub for quick deployment:

- Docker Hub: [https://hub.docker.com/r/bmdarklight/multi-agent-routing](https://hub.docker.com/r/bmdarklight/multi-agent-routing)

To pull and run the image:

```bash
docker pull bmdarklight/multi-agent-routing:latest
docker run -p 8000:8000 bmdarklight/multi-agent-routing:latest
```

---

## 🧪 Testing Requirements

- **Unit Tests** for:
  - Classifier logic (correct routing)
  - Each agent module (math_bot, code_bot, travel_bot)
  - FastAPI endpoints (`/ask`, `/health`)
- **pytest** and **httpx.AsyncClient** for endpoint tests

---

## 📁 Folder Structure

```
.
├── app/
│   ├── main.py           # FastAPI entrypoint
│   ├── agent.py          # LangGraph orchestration
│   ├── classifier.py     # Topic classification logic
│   ├── agents/
│   │   ├── math_bot.py   # MathBot implementation
│   │   ├── code_bot.py   # CodeBot implementation
│   │   └── travel_bot.py # TravelBot implementation
├── tests/
│   ├── test_routing.py
│   ├── test_math_bot.py
│   ├── test_code_bot.py
│   ├── test_travel_bot.py
│   ├── test_api.py
├── Dockerfile
├── docker-compose.yml
├── .github/workflows/
│   └── ci.yml
└── README.md
```

---

## 🚀 Run & Develop

1. **Clone the repository**  
   ```bash
   git clone https://github.com/BMDarkLight/Multi-Agent-Routing.git
   cd Multi-Agent-Routing
   ```

2. **Set environment variables**  
   Create a `.env` file or export necessary environment variables, e.g.:  
   ```bash
   export OPENAI_API_KEY="your_openai_api_key"
   ```

3. **Run locally**  
   Install dependencies and start the FastAPI service:  
   ```bash
   pip install -r requirements.txt
   uvicorn app.main:app --reload
   ```

4. **Run with Docker Compose**  
   Build and start services with Docker Compose:  
   ```bash
   docker-compose up --build
   ```

5. **Run Tests**  
   ```bash
   pytest
   ```
