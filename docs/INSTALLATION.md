# Instalación Detallada - Age of Clans

## Requisitos Previos

- Python 3.8 o superior
- Node.js 14 o superior
- npm o yarn
- Git

## Pasos de Instalación

### 1. Clonar el Repositorio

```bash
git clone https://github.com/clashre/age-of-clans.git
cd age-of-clans
```

### 2. Configurar Backend Python

```bash
# Navega a la carpeta del backend Python
cd backend/python

# Crea un entorno virtual
python -m venv venv

# Activa el entorno virtual
# En Linux/Mac:
source venv/bin/activate

# En Windows:
venv\Scripts\activate

# Instala las dependencias
pip install -r requirements.txt

# Ejecuta el servidor
python -m app.main
```

El servidor Python estará disponible en `http://localhost:8000`

### 3. Configurar Servidor Node.js

```bash
# En otra terminal, navega a la carpeta del backend Node
cd backend/node

# Instala las dependencias
npm install

# Crea archivo .env
cp .env.example .env

# Ejecuta el servidor
npm start
# O para desarrollo con hot-reload:
npm run dev
```

El servidor estará disponible en `http://localhost:3000`

### 4. Acceder al Juego

Abre tu navegador y ve a:
```
http://localhost:3000
```

## Documentación de API

Una vez que el servidor Python está ejecutándose, puedes ver la documentación interactiva:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Solución de Problemas

### Error: "Port already in use"

**Python**: Cambia el puerto en `app/main.py`
```python
uvicorn.run(app, host="0.0.0.0", port=8001)  # Cambiar a otro puerto
```

**Node.js**: Cambia en `backend/node/.env`
```
PORT=3001
```

### Error: "Module not found"

**Python**: Asegúrate de estar en el entorno virtual y ejecuta:
```bash
pip install -r requirements.txt
```

**Node.js**: Ejecuta:
```bash
rm -rf node_modules
npm install
```

### Error de CORS

Los servidores ya tienen CORS configurado, pero si tienes problemas:
- En Python (`app/main.py`), se permite todos los orígenes
- En Node.js (`server.js`), se permite todos los orígenes

## Próximos Pasos

1. Lee [GAME_MECHANICS.md](GAME_MECHANICS.md) para entender las mecánicas
2. Lee [API.md](API.md) para detalles de los endpoints
3. Comienza a desarrollar nuevas características