# 📚 Sistema de Gestión de Biblioteca

Este proyecto es una aplicación web desarrollada con **Python y Django**, que permite la gestión básica de una biblioteca.  
Incluye funcionalidades para administrar libros, autores, stock, préstamos y devoluciones, aplicando reglas de negocio reales.

El sistema fue desarrollado como ejercicio técnico, priorizando:
- Buen diseño de modelos
- Separación de responsabilidades
- Validaciones a nivel de negocio
- Experiencia de usuario básica pero clara

---

## 🚀 Funcionalidades

### 📖 Gestión de Libros
- Crear libros indicando:
  - Título
  - Autor
  - Stock inicial
- Listado de libros con:
  - Autor
  - Stock disponible
- Visualización desde el panel administrativo de Django

### ✍️ Gestión de Autores
- Crear autores
- Asociar autores a libros

### 📦 Gestión de Stock
- Campo de stock integrado al libro
- Ajuste de stock mediante un módulo dedicado:
  - Entradas
  - Salidas
  - Motivo del ajuste
- Registro histórico de todos los movimientos de stock

### 🔄 Préstamos
- Registrar préstamo de un libro:
  - Nombre del solicitante
  - Fecha de préstamo
- Validación:
  - No se permite prestar libros sin stock
- Al confirmar el préstamo:
  - El stock del libro disminuye automáticamente

### 🔁 Devoluciones
- Registrar devolución de libros:
  - Nombre del solicitante
  - Fecha de devolución
- Al confirmar la devolución:
  - El stock del libro aumenta automáticamente

### 🛡️ Validaciones de Negocio
- No se permite stock negativo
- No se permiten préstamos si el stock es 0
- Todas las reglas se validan tanto en frontend como en backend

---

## 🧱 Tecnologías Utilizadas

- Python 3.14
- Django 6.x
- SQLite3
- Bootstrap 5 (CDN)
- Django ORM
- Django Admin

---

## 🗄️ Modelo de Datos (Resumen)

### Entidades principales:
- **Autor**
- **Libro**
- **Prestamo**
- **MovimientoStock**

Relaciones:
- Un autor puede tener muchos libros
- Un libro puede tener múltiples préstamos
- Cada ajuste de stock genera un movimiento registrado

---

## ⚙️ Instalación y Ejecución

1. Clonar el repositorio
git clone <url-del-repositorio>
cd biblioteca
2. Crear el entorno virtual:
python -m venv venv
venv\Scripts\activate
3. Instalar dependencias:
pip install django
4. Ejecutar migraciones
python manage.py makemigrations
python manage.py migrate
5. Crear superusuario
python manage.py createsuperuser
6. Ejecutar servidor
python manage.py runserver
 
