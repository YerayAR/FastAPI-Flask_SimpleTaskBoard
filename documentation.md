# Project Documentation

## 📘 Introducción general del proyecto

Esta aplicación integra un backend mínimo basado en **FastAPI** y un front‑end en **Flask** con estética cyberpunk construida con TailwindCSS. El código implementa:

- Administración de usuarios utilizando **SQLAlchemy** y una base de datos SQLite.
- Validación de datos con **Pydantic**.
- Encriptación de contraseñas con **Passlib** (bcrypt).
- Creación y verificación de tokens JWT con **python-jose**.
- Interfaz web en **Flask** que consume la API mediante Jinja2 y JavaScript.
- Docker y Docker Compose para un despliegue rápido.
- Conjunto de pruebas con **Pytest** tanto para la API como para el front‑end.

La estructura sigue un pequeño patrón modular separando modelos, routers y servicios.

## 📂 Estructura de archivos

```
.
├── backend/                 # Backend FastAPI
├── frontend/            # Front‑end Flask
├── Dockerfile.fastapi
├── Dockerfile.flask
├── docker-compose.yml
└── run.sh
```

```
backend/
├── core/
│   └── security.py
├── database.py
├── main.py
├── models/
│   ├── __init__.py
│   ├── user.py
│   └── task.py
├── routers/
│   ├── __init__.py
│   ├── auth.py
│   ├── items.py
│   └── tasks.py
├── schemas/
│   ├── __init__.py
│   ├── user.py
│   └── task.py
└── services/
    ├── __init__.py
    ├── auth_service.py
    └── task_service.py
```

### Descripción de archivos y carpetas

- **`backend/main.py`**
  - Punto de inicio de la aplicación FastAPI.
  - Incluye los routers y crea las tablas de la base de datos al iniciar.
  - Depende de `routers` y de `database`.

- **`backend/database.py`**
  - Configura la conexión con SQLite y expone `SessionLocal` y la clase base `Base`.
  - Es utilizada por los servicios y por `main.py` para inicializar la base de datos.

- **`backend/core/security.py`**
  - Funciones de seguridad: hashing de contraseñas y generación/verificación de tokens JWT.
  - Utiliza `passlib` y `python-jose`.

- **`backend/models/user.py`**
  - Modelo ORM de SQLAlchemy que representa la tabla `users`.
  - Importado por los servicios para realizar operaciones de base de datos.
- **`backend/models/task.py`**
  - Modelo ORM que almacena tareas simples para la demo.

- **`backend/routers/auth.py`**
  - Endpoints para registro y login de usuarios.
  - Depende del servicio `auth_service` y de los esquemas de `schemas`.

- **`backend/routers/items.py`**
  - Endpoint protegido que devuelve el usuario autenticado.
  - Utiliza `get_current_user` del servicio de autenticación.

- **`backend/routers/tasks.py`**
  - Endpoints para crear y listar tareas de ejemplo.
  - Depende del servicio `task_service`.

- **`backend/schemas/user.py`**
  - Esquemas Pydantic para entrada y salida de datos de usuario y tokens.
- **`backend/schemas/task.py`**
  - Define los modelos de datos para las tareas.

- **`backend/services/auth_service.py`**
  - Conjunto de funciones de negocio para gestionar usuarios y autenticación.
  - Interactúa con la base de datos y con el módulo `security`.

- **`backend/services/task_service.py`**
  - Operaciones CRUD de tareas utilizadas por el router de tareas.

- **`tests/test_auth.py`**
  - Pruebas Pytest que verifican el flujo de registro, login y acceso a rutas protegidas.
- **`tests/test_flask.py`**
  - Comprueba que la página principal de Flask se renderiza correctamente.
- **`tests/test_tasks.py`**
  - Valida la API de tareas del backend.

- **`frontend/`**
  - Contiene la aplicación Flask: `app.py`, blueprints y plantillas Jinja2.
- **`Dockerfile.fastapi`** y **`Dockerfile.flask`**
  - Imágenes Docker para cada servicio.
- **`docker-compose.yml`**
  - Orquestación de ambos contenedores.
- **`run.sh`**
  - Script simplificado para arrancar y apagar la pila con Docker Compose.

## 🔁 Diagrama de interconexión

```
[ FastAPI app ]
      |-- includes --> [auth router] -- uses --> [auth_service] -- uses --> [database]
      |                       |                               |
      |                       |                               +--> [models.User]
      |                       |
      |                       +--> [security] & [schemas]
      |
      |-- includes --> [items router] -- uses --> [auth_service.get_current_user]
```

Los módulos de pruebas (`tests/test_auth.py`, `tests/test_flask.py`, `tests/test_tasks.py`) actúan como clientes externos que realizan peticiones HTTP al **FastAPI app** y validan la interfaz.
