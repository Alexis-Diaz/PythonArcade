# PythonArcade
Python Arcade es una aplicación web desarrollada con Flask que reúne varios minijuegos interactivos en una sola plataforma. El proyecto incluye Piedra, Papel o Tijera, Adivina el Número y Memorama de Emojis. Fue diseñado como práctica de programación web utilizando Python, HTML, CSS y JavaScript, aplicando conceptos como rutas, sesiones, generación de números aleatorios, manipulación del DOM y diseño responsivo para dispositivos móviles.

# 🎮 Python Arcade

Python Arcade es una plataforma web de minijuegos desarrollada con **Flask**, **HTML**, **CSS** y **JavaScript**. El objetivo del proyecto es demostrar la integración entre frontend y backend mediante juegos sencillos, interactivos y fáciles de comprender.

## 📌 Características

* Interfaz web moderna y responsiva.
* Compatible con computadoras y dispositivos móviles.
* Desarrollo utilizando Python y Flask.
* Código comentado para facilitar el aprendizaje.
* Navegación entre distintos juegos desde un menú principal.

---

# 🕹️ Juegos incluidos

## ✂️ Piedra, Papel o Tijera

Compite contra la computadora en un torneo de varias rondas.

### Funcionalidades

* Selección de número de rondas.
* Marcador en tiempo real.
* Elección aleatoria de la computadora.
* Detección automática del ganador.
* Reinicio de partida.

### Conceptos utilizados

* Condicionales.
* Funciones.
* Números aleatorios.
* Comunicación cliente-servidor mediante JSON.

---

## 🎯 Adivina el Número

La computadora genera un número secreto que el jugador debe descubrir.

### Funcionalidades

* Tres niveles de dificultad.
* Indicaciones de si el número es mayor o menor.
* Contador de intentos.
* Reinicio automático de partidas.

### Conceptos utilizados

* Variables.
* Sesiones en Flask.
* Números aleatorios.
* Validación de datos.

---

## 🧠 Memorama de Emojis

Encuentra todas las parejas ocultas en el menor número de movimientos posible.

### Funcionalidades

* Barajado aleatorio de cartas.
* Contador de movimientos.
* Contador de parejas encontradas.
* Botón de nuevo juego.
* Detección de victoria.

### Conceptos utilizados

* Manipulación del DOM.
* Eventos en JavaScript.
* Arreglos y funciones.
* Programación orientada a eventos.

---

# 🛠️ Tecnologías utilizadas

* Python 3
* Flask
* HTML5
* CSS3
* JavaScript
* JSON

---

# 📂 Estructura del proyecto

```text
PythonArcade/

│ app.py

├── templates/
│   ├── index.html
│   ├── piedra_papel_tijera.html
│   ├── adivina_numero.html
│   └── memorama.html

├── static/
│   ├── style.css
│   └── arcade.css

└── requirements.txt
```

---

# 🚀 Instalación

Clonar el repositorio:

```bash
git clone https://github.com/tu-usuario/python-arcade.git
```

Entrar al directorio:

```bash
cd python-arcade
```

Instalar dependencias:

```bash
pip install -r requirements.txt
```

Ejecutar la aplicación:

```bash
python app.py
```

Abrir en el navegador:

```text
http://127.0.0.1:5000
```

---

# 🎯 Objetivos de aprendizaje

Este proyecto fue desarrollado para practicar:

* Desarrollo web con Flask.
* Creación de rutas y vistas.
* Uso de sesiones.
* Diseño responsivo.
* Interacción entre frontend y backend.
* Programación con JavaScript.
* Organización de proyectos web.

---

# 📱 Diseño responsivo

La interfaz se adapta automáticamente a:

* Computadoras de escritorio.
* Tablets.
* Teléfonos móviles.

---

# 📄 Licencia

Proyecto desarrollado con fines educativos y de aprendizaje.
Todos los recursos utilizados son de libre uso académico.
