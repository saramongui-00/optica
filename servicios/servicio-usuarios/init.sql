CREATE DATABASE IF NOT EXISTS db_usuarios;
USE db_usuarios;

CREATE TABLE IF NOT EXISTS usuarios (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(100) NOT NULL,
  user VARCHAR(50) NOT NULL UNIQUE,
  celular BIGINT NOT NULL,
  email VARCHAR(100) NOT NULL,
  password VARCHAR(255) NOT NULL,
  estado ENUM('HABILITADO', 'DESHABILITADO') DEFAULT 'HABILITADO',
  rol ENUM('OPTOMETRA', 'SECRETARIO') NOT NULL DEFAULT 'SECRETARIO'
);

INSERT IGNORE INTO usuarios (nombre, user, celular, email, password, estado, rol) VALUES
('Diana', 'diana', 3001234567, 'diana@optica.com', '$2b$10$9rSujxFkFC8KVF.GfklGw.ZgyO7QntCSM83sLdhOWmPT2gJYD8ZD6', 'HABILITADO', 'OPTOMETRA'),
('Carlos Ruiz', 'carlos', 3109876543, 'carlos@optica.com', '$2b$10$9rSujxFkFC8KVF.GfklGw.ZgyO7QntCSM83sLdhOWmPT2gJYD8ZD6', 'HABILITADO', 'SECRETARIO'),
('María López', 'maria', 3205556789, 'maria@optica.com', '$2b$10$9rSujxFkFC8KVF.GfklGw.ZgyO7QntCSM83sLdhOWmPT2gJYD8ZD6', 'HABILITADO', 'SECRETARIO');