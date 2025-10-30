# Proyecto de Figuras Geométricas con TDD

Un proyecto en Python que implementa figuras geométricas (Rectángulo, Círculo y Triángulo) utilizando la metodología de Desarrollo Dirigido por Pruebas (TDD).

## Estructura del Proyecto

```
src/
├── rectangulo/      # Implementación del Rectángulo
├── circulo/         # Implementación del Círculo
└── triangulo/       # Implementación del Triángulo

tests/
├── test_rectangulo/ # Pruebas del Rectángulo
├── test_circulo/    # Pruebas del Círculo
└── test_triangulo/  # Pruebas del Triángulo
```

## Configuración

1. Crear un entorno virtual:
```bash
python -m venv env
```

2. Activar el entorno virtual:
- Windows:
```bash
.\env\Scripts\activate
```
- Unix/MacOS:
```bash
source env/bin/activate
```

3. Instalar dependencias:
```bash
pip install -r requirements.txt
```

## Pruebas

Para ejecutar las pruebas:
```bash
pytest
```

## Componentes del Proyecto

### Rectángulo
- Implementación: `src/rectangulo/rectangulo.py`
- Pruebas: `tests/test_rectangulo/test_rectangulo.py`

### Círculo
- Implementación: `src/circulo/circulo.py`
- Pruebas: `tests/test_circulo/test_circulo.py`

### Triángulo
- Implementación: `src/triangulo/triangulo.py`
- Pruebas: `tests/test_triangulo/test_triangulo.py`

## Enfoque de Desarrollo

Este proyecto sigue los principios de Desarrollo Dirigido por Pruebas (TDD):
1. Escribir una prueba que falle
2. Escribir el código mínimo para que la prueba pase
3. Refactorizar el código manteniendo las pruebas en verde