# Pre-Entrega – Automatización Web con SauceDemo

## Propósito

Proyecto de la pre-entrega de Automatización Web. Automatiza una compra básica en
[SauceDemo](https://www.saucedemo.com/) y valida tres flujos principales:

1. **Login**: acceso con usuario y contraseña, validando la URL (`/inventory.html`) y el título *Products*.
2. **Catálogo**: título de la página, productos visibles, menú, filtro, y nombre/precio del primer producto.
3. **Carrito**: agregar el primer producto, validar el contador del carrito y comprobar el producto dentro del carrito.

## Tecnologías

| Tecnología | Uso |
|---|---|
| Python 3 | Lenguaje del proyecto |
| Selenium WebDriver | Automatización del navegador (Chrome) |
| Pytest | Ejecución y validación de los tests |
| pytest-html | Generación del reporte HTML |
| Git / GitHub | Control de versiones y entrega |

## Estructura del proyecto

```
pre-entrega-automation-testing-nicolas-olivari/
├── tests/
│   ├── test_login.py          # test_login_exitoso
│   ├── test_inventory.py      # test_catalogo
│   └── test_cart.py           # test_cart
├── utils/
│   └── funciones_auxiliares.py  # funciones reutilizables (login, primer producto)
├── reports/                   # reporte HTML generado con Pytest
├── pytest.ini
├── requirements.txt
└── README.md
```

## Instalación

Requisitos: Python 3 y Google Chrome instalados.

```bash
# 1. Clonar el repositorio
git clone https://github.com/nnoqatesting/Automatizacion-talento-tech-
cd pre-entrega-automation-testing-nicolas-olivari

# 2. Crear y activar un entorno virtual
python -m venv .venv
.venv\Scripts\activate        # Windows
# source .venv/bin/activate   # macOS / Linux

# 3. Instalar dependencias
pip install -r requirements.txt
```

## Ejecución

Correr todos los tests:

```bash
pytest -v
```

Correr los tests y generar el reporte HTML:

```bash
pytest -v --html=reports/reporte.html --self-contained-html
```

Correr un test puntual:

```bash
pytest -v tests/test_login.py
```

Para ver el nombre y precio del primer producto impresos en consola, agregar `-s`:

```bash
pytest -v -s tests/test_inventory.py
```

## Reporte

El reporte HTML se genera en `reports/reporte.html`.

## Autor

Nicolas Olivari
