<div align="center">

<br/>

```
 ██████╗ ██████╗ ████████╗██╗ ██████╗ █████╗
██╔═══██╗██╔══██╗╚══██╔══╝██║██╔════╝██╔══██╗
██║   ██║██████╔╝   ██║   ██║██║     ███████║
██║   ██║██╔═══╝    ██║   ██║██║     ██╔══██║
╚██████╔╝██║        ██║   ██║╚██████╗██║  ██║
 ╚═════╝ ╚═╝        ╚═╝   ╚═╝ ╚═════╝╚═╝  ╚═╝
```

### Sistema de Información para Gestión de Citas y Exámenes Médicos en Óptica

<br/>

![Java](https://img.shields.io/badge/Java-ED8B00?style=for-the-badge&logo=openjdk&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![Spring Boot](https://img.shields.io/badge/Spring_Boot-6DB33F?style=for-the-badge&logo=spring-boot&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Node.js](https://img.shields.io/badge/Node.js-339933?style=for-the-badge&logo=nodedotjs&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB-4EA94B?style=for-the-badge&logo=mongodb&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)

<br/>

</div>

---

## 📋 Tabla de Contenidos

- [Descripción](#-descripción)
- [Arquitectura](#-arquitectura)
- [Microservicios](#-microservicios)
- [Tecnologías](#-tecnologías)
- [Requisitos Previos](#-requisitos-previos)
- [Instalación y Configuración](#-instalación-y-configuración)
- [Endpoints](#-endpoints)
- [Estructura del Proyecto](#-estructura-del-proyecto)
- [Equipo](#-equipo)

---

## 📌 Descripción

**Optica** es un sistema de información desarrollado bajo **arquitectura de microservicios** para la gestión integral de una óptica: autenticación de usuarios, gestión de personal, agendamiento de citas, registro de pacientes e historial clínico con exámenes visuales completos.

Desarrollado como proyecto académico para la materia **Ingeniería de Software II** — Universidad Pedagógica y Tecnológica de Colombia (UPTC).

---

## 🏗 Arquitectura

```
                        ┌─────────────────┐
                        │    Frontend     │
                        │   (Puerto 3000) │
                        └────────┬────────┘
                                 │
                        ┌────────▼────────┐
                        │  API Gateway    │
                        │ Spring Eureka   │
                        │  (Puerto 8761)  │
                        └────────┬────────┘
                                 │
          ┌──────────────────────┼──────────────────────┐
          │              ┌───────┴────────┐             │
          │              │                │             │
   ┌──────▼──────┐ ┌─────▼──────┐ ┌──────▼──────┐      │
   │    Auth     │ │  Usuarios  │ │    Citas    │      │
   │  JS/Node    │ │  JS/Node   │ │   Python    │      │
   │  Port 8081  │ │  Port 8082 │ │  Port 8083  │      │
   └──────┬──────┘ └─────┬──────┘ └──────┬──────┘      │
          │              │               │             │
          │         ┌────▼────┐   ┌──────▼──────┐      │
          │         │PostgreSQL│   │  Pacientes  │      │
          └────────►│  :5432  │   │   Python    │      │
                    └─────────┘   │  Port 8084  │      │
                                  └──────┬──────┘      │
                              ┌──────────▼──────────┐  │
                              │       MongoDB       │  │
                              │       :27017        │  │
                              └─────────────────────┘  │
                                                        │
                              ┌─────────────────────┐  │
                              │  Historial Clínico  ◄──┘
                              │    Java/Spring      │
                              │     Port 8085       │
                              └──────────┬──────────┘
                                         │
                              ┌──────────▼──────────┐
                              │       MongoDB       │
                              │       :27018        │
                              └─────────────────────┘
```

---

## ⚙️ Microservicios

| # | Microservicio | Lenguaje / Framework | Base de Datos | Puerto |
|---|---|---|---|---|
| 1 | **ms-autenticacion** | Node.js + Express | PostgreSQL | 8081 |
| 2 | **ms-usuarios** | Node.js + Express | PostgreSQL | 8082 |
| 3 | **ms-citas** | Python + FastAPI | MongoDB | 8083 |
| 4 | **ms-pacientes** | Python + FastAPI | MongoDB | 8084 |
| 5 | **ms-historial** | Java + Spring Boot | MongoDB | 8085 |

### ms-autenticacion
Gestiona el acceso al sistema mediante autenticación con **JWT (JSON Web Tokens)**. Implementa el patrón arquitectónico *Access Token*.

- `POST /auth/login` — Iniciar sesión
- `POST /auth/logout` — Cerrar sesión
- `POST /auth/validate` — Validar token

### ms-usuarios
Administración del personal del sistema (optómetras y asistentes).

- `POST /usuarios` — Registrar usuario
- `GET /usuarios/{id}` — Consultar usuario
- `PUT /usuarios/{id}` — Modificar usuario
- `PATCH /usuarios/{id}/inhabilitar` — Inhabilitar usuario

### ms-citas
Gestión del agendamiento de citas médicas.

- `POST /citas` — Crear cita
- `GET /citas/{id}` — Consultar cita
- `PUT /citas/{id}` — Modificar cita
- `DELETE /citas/{id}` — Cancelar cita
- `PATCH /citas/{id}/confirmar` — Confirmar cita

### ms-pacientes
Registro y administración de la información de pacientes.

- `POST /pacientes` — Registrar paciente
- `GET /pacientes/{id}` — Consultar paciente
- `PUT /pacientes/{id}` — Modificar paciente
- `DELETE /pacientes/{id}` — Eliminar paciente

### ms-historial
Gestión del historial clínico y documentación de exámenes visuales completos.

- `POST /historial` — Crear historia clínica
- `GET /historial/{id}` — Consultar historial
- `POST /historial/{id}/examen` — Documentar examen visual
- `GET /historial/{id}/examen/{examenId}` — Consultar examen
- `GET /historial/{id}/documento` — Generar documento HC
- `GET /historial/{id}/rx` — Generar Rx final

---

## 🛠 Tecnologías

| Capa | Tecnología |
|---|---|
| API Gateway | Spring Eureka (Spring Cloud Netflix) |
| Autenticación | JWT (JSON Web Tokens) |
| ORM (Java) | Hibernate + JPA |
| ORM (Python) | SQLAlchemy / Motor (async MongoDB) |
| BD Relacional | PostgreSQL 15 |
| BD NoSQL | MongoDB 7 |
| Contenerización | Docker + Docker Compose |
| Frontend | *(a definir por el grupo)* |

---

## ✅ Requisitos Previos

Antes de correr el proyecto necesitas tener instalado:

- [Docker Desktop](https://www.docker.com/products/docker-desktop/) (incluye Docker Compose)
- [Git](https://git-scm.com/)
- JDK 21 (solo si vas a desarrollar `ms-historial` sin Docker)
- Node.js 20+ (solo si vas a desarrollar `ms-autenticacion` o `ms-usuarios` sin Docker)
- Python 3.11+ (solo si vas a desarrollar `ms-citas` o `ms-pacientes` sin Docker)

---

## 🚀 Instalación y Configuración

### 1. Clonar el repositorio

```bash
git clone https://github.com/tu-usuario/optica.git
cd optica
```

### 2. Levantar la infraestructura (bases de datos + Eureka)

```bash
docker compose up --build
```

Esto levanta automáticamente:
- Spring Eureka en `http://localhost:8761`
- PostgreSQL en el puerto `5432`
- MongoDB (instancia 1) en el puerto `27017`
- MongoDB (instancia 2) en el puerto `27018`

### 3. Verificar que Eureka está corriendo

Abre `http://localhost:8761` en el navegador. Deberías ver el dashboard de Eureka.

### 4. Levantar cada microservicio

Cada microservicio tiene su propio `README.md` con instrucciones de configuración. En general:

```bash
# ms-autenticacion y ms-usuarios (Node.js)
cd ms-autenticacion
npm install
npm run dev

# ms-citas y ms-pacientes (Python)
cd ms-citas
pip install -r requirements.txt
uvicorn main:app --reload --port 8083

# ms-historial (Java)
cd ms-historial
./mvnw spring-boot:run
```

---

## 📁 Estructura del Proyecto

```
optica/
│
├── docker-compose.yml          ← Infraestructura completa
│
├── eureka-server/              ← API Gateway
│   ├── src/
│   ├── Dockerfile
│   └── pom.xml
│
├── ms-autenticacion/           ← Node.js + Express
│   ├── src/
│   ├── Dockerfile
│   └── package.json
│
├── ms-usuarios/                ← Node.js + Express
│   ├── src/
│   ├── Dockerfile
│   └── package.json
│
├── ms-citas/                   ← Python + FastAPI
│   ├── app/
│   ├── Dockerfile
│   └── requirements.txt
│
├── ms-pacientes/               ← Python + FastAPI
│   ├── app/
│   ├── Dockerfile
│   └── requirements.txt
│
├── ms-historial/               ← Java + Spring Boot
│   ├── src/
│   ├── Dockerfile
│   └── pom.xml
│
└── frontend/                   ← Interfaz web
    └── ...
```

---

## 👥 Equipo

Desarrollado por estudiantes de **Ingeniería de Sistemas — UPTC**
Materia: Ingeniería de Software II · 2026

---

<div align="center">

**Universidad Pedagógica y Tecnológica de Colombia**
Facultad de Ingeniería · Escuela de Ingeniería de Sistemas

</div>
