# 🚀 Cyberpunk Task Board

> **A futuristic task management application combining FastAPI backend with Flask frontend**

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-Latest-green.svg)](https://fastapi.tiangolo.com/)
[![Flask](https://img.shields.io/badge/Flask-Latest-red.svg)](https://flask.palletsprojects.com/)

## ⚡ Quick Start

### 🎯 One-Command Setup (Recommended)

**Windows:**
```bash
python scripts/start.py
```
*OR double-click `scripts/start.bat`*

**macOS/Linux:**
```bash
python3 scripts/start.py
```
*OR run `scripts/start.sh`*

### 🌟 That's it! 
The application will:
- ✅ Automatically create a virtual environment
- ✅ Install all dependencies
- ✅ Start both servers (FastAPI + Flask)
- ✅ Open your browser to http://localhost:5000

---

## 🎮 What You'll Get

- **🎯 Task Management**: Create, view, and delete tasks
- **🔐 Authentication**: Secure JWT-based login system
- **🎨 Cyberpunk UI**: Futuristic interface with TailwindCSS
- **📱 Responsive**: Works on desktop and mobile
- **⚡ Real-time**: Automatic updates and live reload

## 🛠️ Technology Stack
| Component | Technology |
|-----------|------------|
| **Backend** | FastAPI + SQLAlchemy + SQLite |
| **Frontend** | Flask + Jinja2 + TailwindCSS |
| **Auth** | JWT + Passlib (bcrypt) |
| **Testing** | Pytest with coverage |
| **Deployment** | Docker + Docker Compose |

## 📁 Project Structure

``` 
📦 cyberpunk-task-board/
├── scripts/               # Utilidades de arranque
│   ├── start.py           # Script universal
│   ├── start.sh           # Linux/macOS
│   ├── start.bat          # Windows
│   ├── start_fastapi.bat  # API en Windows
│   └── start_flask.bat    # Frontend en Windows
├── backend/              # Backend FastAPI
│   ├── main.py            # Punto de entrada
│   ├── config/            # Configuración (DB, etc.)
│   ├── controllers/       # Endpoints HTTP
│   ├── models/            # Modelos ORM
│   ├── schemas/           # Esquemas de validación
│   ├── services/          # Lógica de negocio
│   └── utils/             # Funciones auxiliares
├── frontend/             # Frontend Flask
│   ├── app.py             # Entrada Flask
│   ├── routes/            # Rutas web
│   ├── templates/         # Plantillas HTML
│   └── static/            # Archivos estáticos
├── tests/                 # Pruebas automatizadas
├── docker-compose.yml     # Orquestación con Docker
└── requirements.txt       # Dependencias Python
``` 

## 🔗 API Endpoints

### Authentication
- **POST** `/register` - Create new user account
- **POST** `/token` - Login and get JWT token

### Tasks
- **GET** `/tasks/` - List all tasks
- **POST** `/tasks/` - Create new task
- **DELETE** `/tasks/{task_id}` - Delete task

### User
- **GET** `/items/me` - Get current user info
- **GET** `/` - Health check

**🔍 Interactive API Documentation**: http://localhost:8000/docs

---

## 🐳 Alternative: Docker Setup

If you prefer Docker:

```bash
# Start everything with Docker
docker compose up --build

# Stop everything
docker compose down
```

**Access Points:**
- 🌐 **Frontend**: http://localhost:5000
- 🔧 **API**: http://localhost:8000
- 📚 **API Docs**: http://localhost:8000/docs

---

## 🧪 Testing

```bash
# Run all tests with coverage
python scripts/start.py && pytest --cov

# Or if already set up:
pytest --cov
```

---

## 🛠️ Manual Setup (Advanced Users)

If you prefer manual setup:

**1. Setup Environment:**
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

**2. Start FastAPI:**
```bash
uvicorn backend.main:app --reload
```

**3. Start Flask (in new terminal):**
```bash
export FASTAPI_URL=http://localhost:8000  # Windows: set FASTAPI_URL=...
python -m frontend.app
```

---

## 🎯 Features

- ✅ **User Registration & Login**
- ✅ **JWT Authentication**
- ✅ **Task CRUD Operations**
- ✅ **Responsive Cyberpunk UI**
- ✅ **Real-time Updates**
- ✅ **SQLite Database**
- ✅ **Docker Support**
- ✅ **Comprehensive Tests**
- ✅ **API Documentation**

---

## 🔧 Troubleshooting

**❓ Application won't start?**
- Ensure Python 3.8+ is installed
- Check if ports 5000 and 8000 are available
- Try: `python --version` and `pip --version`

**❓ "Module not found" errors?**
- The startup script handles this automatically
- Manual fix: `pip install -r requirements.txt`

**❓ Can't access in browser?**
- Check if firewall is blocking ports 5000/8000
- Try http://127.0.0.1:5000 instead of localhost

---

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch: `git checkout -b feature/amazing-feature`
3. Commit changes: `git commit -m 'Add amazing feature'`
4. Push to branch: `git push origin feature/amazing-feature`
5. Open a Pull Request

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

**Created by Yeray Alonso Reyes**

---

### 🌟 Star this repo if you found it helpful!
