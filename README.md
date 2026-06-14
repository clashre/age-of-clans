# Age of Clans 🏰

Un juego de estrategia single-player inspirado en Clash of Clans, construido con Python (FastAPI) + Node.js/Express y una interfaz web moderna.

## 📋 Descripción

Age of Clans es un juego de construcción y administración de aldea donde los jugadores pueden:
- Construir y mejorar estructuras
- Entrenar tropas
- Participar en combates PvE
- Gestionar recursos (oro, elixir)
- Progresar a través de múltiples niveles
- Realizar investigaciones para mejorar unidades

## 🎮 Características

### Sistema de Aldea
- Construcción de estructuras (barracones, almacenes, laboratorio, etc.)
- Sistema de niveles de construcción
- Grid de colocación de estructuras

### Sistema de Recursos
- Oro y Elixir como recursos principales
- Generación pasiva de recursos
- Almacenes con capacidad limitada

### Sistema de Tropas
- Múltiples tipos de unidades (Barbarian, Archer, Giant, etc.)
- Entrenamientos con tiempo y costo
- Sistema de niveles de tropas

### Sistema de Combate
- Ataques contra enemigos PvE
- Cálculo de daño realista
- Recompensas por victoria
- Penalizaciones por derrota

### Sistema de Progresión
- Niveles de ayuntamiento
- Investigaciones en laboratorio
- Desbloqueo de nuevas estructuras y tropas

## 📁 Estructura del Proyecto

```
age-of-clans/
├── backend/
│   ├── python/
│   │   ├── app/
│   │   │   ├── __init__.py
│   │   │   ├── main.py
│   │   │   ├── models/
│   │   │   ├── routes/
│   │   │   ├── services/
│   │   │   └── database/
│   │   ├── requirements.txt
│   │   └── README.md
│   └── node/
│       ├── server.js
│       ├── package.json
│       └── routes/
├── frontend/
│   ├── index.html
│   ├── css/
│   ├── js/
│   └── assets/
├── docs/
│   ├── API.md
│   ├── GAME_MECHANICS.md
│   └── INSTALLATION.md
└── config/
    └── settings.json
```

## 🛠️ Tecnologías

- **Backend Principal**: FastAPI (Python)
- **Servidor Web**: Express (Node.js)
- **Base de Datos**: SQLite (desarrollo) / PostgreSQL (producción)
- **Frontend**: HTML5, CSS3, JavaScript Vanilla
- **Canvas/Gráficos**: Phaser 3 o PixiJS

## 🚀 Inicio Rápido

### Requisitos
- Python 3.8+
- Node.js 14+
- npm o yarn

### Instalación

1. Clona el repositorio
```bash
git clone https://github.com/clashre/age-of-clans.git
cd age-of-clans
```

2. Configura el backend Python
```bash
cd backend/python
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
pip install -r requirements.txt
python -m app.main
```

3. Configura el servidor Node.js
```bash
cd backend/node
npm install
npm start
```

4. Abre el cliente web
```
http://localhost:3000
```

## 📖 Documentación

- [API Reference](docs/API.md)
- [Mecánicas del Juego](docs/GAME_MECHANICS.md)
- [Instalación Detallada](docs/INSTALLATION.md)

## 📝 Licencia

MIT License - Ver LICENSE para más detalles

## 👨‍💻 Contribuyentes

- clashre (Developer)

---

**Versión**: 0.1.0  
**Estado**: En Desarrollo
