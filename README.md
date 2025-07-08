# AI Training Project: Multi-Agent Question Routing System

## 🎯 Objective

Build a containerized FastAPI service that implements a **LangGraph-based multi-agent routing system**. The service should classify incoming questions and route them to specialized agents (MathBot, CodeBot, TravelBot), returning their responses via a clean API.

---

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

1. **Start services**  
   ```bash
   docker-compose up --build
   ```

2. **Codespaces**  
   - Open in GitHub Codespaces
   - Connect via vscode extension 

3. **Run Tests**  
   ```bash
   pytest
   ```

