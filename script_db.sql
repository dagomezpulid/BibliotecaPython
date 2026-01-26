-- Tabla Autores
CREATE TABLE catalogo_autor (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre VARCHAR(100) NOT NULL
);

-- Tabla Libros
CREATE TABLE catalogo_libro (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo VARCHAR(200) NOT NULL,
    autor_id INTEGER NOT NULL,
    FOREIGN KEY (autor_id) REFERENCES catalogo_autor(id)
);
