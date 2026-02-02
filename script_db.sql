-- ============================
-- Tabla Autores
-- ============================
CREATE TABLE catalogo_autor (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre VARCHAR(100) NOT NULL
);

-- ============================
-- Tabla Libros
-- ============================
CREATE TABLE catalogo_libro (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo VARCHAR(200) NOT NULL,
    autor_id INTEGER NOT NULL,
    stock INTEGER NOT NULL DEFAULT 0 CHECK (stock >= 0),
    FOREIGN KEY (autor_id) REFERENCES catalogo_autor(id)
);

-- ============================
-- Tabla Préstamos
-- ============================
CREATE TABLE catalogo_prestamo (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    libro_id INTEGER NOT NULL,
    solicitante VARCHAR(100) NOT NULL,
    fecha_prestamo DATE NOT NULL,
    fecha_devolucion DATE,
    FOREIGN KEY (libro_id) REFERENCES catalogo_libro(id)
);

-- ============================
-- Tabla Movimientos de Stock
-- ============================
CREATE TABLE catalogo_movimientostock (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    libro_id INTEGER NOT NULL,
    tipo VARCHAR(10) NOT NULL CHECK (tipo IN ('ENTRADA', 'SALIDA')),
    cantidad INTEGER NOT NULL CHECK (cantidad > 0),
    motivo VARCHAR(200) NOT NULL,
    fecha DATETIME NOT NULL,
    FOREIGN KEY (libro_id) REFERENCES catalogo_libro(id)
);
