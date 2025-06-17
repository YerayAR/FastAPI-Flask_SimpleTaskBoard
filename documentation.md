# Project Documentation

## 📘 Introducción general del proyecto

Esta aplicación es un ejemplo mínimo construido con **FastAPI** para demostrar un flujo básico de autenticación mediante JWT. El código implementa:

- Administración de usuarios utilizando **SQLAlchemy** y una base de datos SQLite.
- Validación de datos con **Pydantic**.
- Encriptación de contraseñas con **Passlib** (bcrypt).
- Creación y verificación de tokens JWT con **python-jose**.
- Conjunto de pruebas con **Pytest** y `TestClient` de FastAPI.

La estructura sigue un pequeño patrón modular separando modelos, routers y servicios.

## 📂 Estructura de archivos

```
app/
├── core/
│   └── security.py
├── database.py
├── main.py
├── models/
│   ├── __init__.py
│   └── user.py
├── routers/
│   ├── __init__.py
│   ├── auth.py
│   └── items.py
├── schemas/
│   ├── __init__.py
│   └── user.py
└── services/
    ├── __init__.py
    └── auth_service.py
```

### Descripción de archivos y carpetas

- **`app/main.py`**
  - Punto de inicio de la aplicación FastAPI.
  - Incluye los routers y crea las tablas de la base de datos al iniciar.
  - Depende de `routers` y de `database`.

- **`app/database.py`**
  - Configura la conexión con SQLite y expone `SessionLocal` y la clase base `Base`.
  - Es utilizada por los servicios y por `main.py` para inicializar la base de datos.

- **`app/core/security.py`**
  - Funciones de seguridad: hashing de contraseñas y generación/verificación de tokens JWT.
  - Utiliza `passlib` y `python-jose`.

- **`app/models/user.py`**
  - Modelo ORM de SQLAlchemy que representa la tabla `users`.
  - Importado por los servicios para realizar operaciones de base de datos.

- **`app/routers/auth.py`**
  - Endpoints para registro y login de usuarios.
  - Depende del servicio `auth_service` y de los esquemas de `schemas`.

- **`app/routers/items.py`**
  - Endpoint protegido que devuelve el usuario autenticado.
  - Utiliza `get_current_user` del servicio de autenticación.

- **`app/schemas/user.py`**
  - Esquemas Pydantic para entrada y salida de datos de usuario y tokens.

- **`app/services/auth_service.py`**
  - Conjunto de funciones de negocio para gestionar usuarios y autenticación.
  - Interactúa con la base de datos y con el módulo `security`.

- **`tests/test_auth.py`**
  - Pruebas Pytest que verifican el flujo de registro, login y acceso a rutas protegidas.

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

El módulo de pruebas (`tests/test_auth.py`) actúa como cliente externo que hace peticiones HTTP al **FastAPI app**.
