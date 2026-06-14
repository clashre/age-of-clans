# API Reference - Age of Clans

## Base URL

```
http://localhost:8000
```

## Authentication

Actualmente sin autenticación (desarrollo). Se implementará JWT en futuras versiones.

## Endpoints

### Health Check

```http
GET /health
```

Respuesta:
```json
{
  "status": "ok",
  "version": "0.1.0"
}
```

### Aldea

#### Obtener Aldea

```http
GET /villages/{village_id}
```

Respuesta:
```json
{
  "id": 1,
  "player_id": 1,
  "name": "Mi Aldea",
  "level": 1,
  "gold": 1000,
  "elixir": 500,
  "experience": 0,
  "created_at": "2024-01-01T00:00:00",
  "updated_at": "2024-01-01T00:00:00"
}
```

#### Crear Aldea

```http
POST /villages
Content-Type: application/json

{
  "player_id": 1,
  "name": "Mi Aldea"
}
```

### Construcciones

#### Obtener Construcciones

```http
GET /villages/{village_id}/buildings
```

Respuesta:
```json
[
  {
    "id": 1,
    "village_id": 1,
    "building_type": "townhall",
    "level": 1,
    "x": 9,
    "y": 7,
    "is_constructing": false,
    "construction_start": null,
    "construction_end": null
  }
]
```

#### Crear Construcción

```http
POST /villages/{village_id}/buildings
Content-Type: application/json

{
  "building_type": "barracks",
  "x": 7,
  "y": 5
}
```

#### Mejorar Construcción

```http
PUT /buildings/{building_id}
Content-Type: application/json

{
  "action": "upgrade"
}
```

### Tropas

#### Obtener Tropas

```http
GET /villages/{village_id}/troops
```

Respuesta:
```json
[
  {
    "id": 1,
    "village_id": 1,
    "troop_type": "barbarian",
    "quantity": 10,
    "level": 1,
    "is_training": false
  }
]
```

#### Entrenar Tropas

```http
POST /villages/{village_id}/troops
Content-Type: application/json

{
  "troop_type": "barbarian",
  "quantity": 5
}
```

### Investigación

#### Obtener Investigaciones

```http
GET /villages/{village_id}/researches
```

#### Iniciar Investigación

```http
POST /villages/{village_id}/researches
Content-Type: application/json

{
  "research_type": "troop_damage"
}
```

### Combate

#### Iniciar Ataque

```http
POST /villages/{village_id}/attack
Content-Type: application/json

{
  "enemy_village_id": 2,
  "troops": [
    {
      "troop_type": "barbarian",
      "quantity": 5
    },
    {
      "troop_type": "archer",
      "quantity": 3
    }
  ]
}
```

Respuesta:
```json
{
  "success": true,
  "damage_dealt": 150,
  "damage_taken": 45,
  "gold_earned": 500,
  "troops_lost": 2
}
```

## Códigos de Error

- `200`: OK
- `201`: Created
- `400`: Bad Request
- `404`: Not Found
- `409`: Conflict
- `500`: Internal Server Error

## Rate Limiting

Actualmente sin limitación. Se implementará en versiones futuras.