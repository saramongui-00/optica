const pool = require('../config/db');

const guardar = async (usuario) => {
  const [result] = await pool.query(
    `INSERT INTO usuarios (nombre, user, celular, email, password, estado, rol)
     VALUES (?, ?, ?, ?, ?, ?, ?)`,
    [usuario.nombre, usuario.user, usuario.celular,
     usuario.email, usuario.password, usuario.estado, usuario.rol]
  );
  return result;
};

const actualizar = async (usuario) => {
  const [result] = await pool.query(
    `UPDATE usuarios SET nombre = ?, celular = ?, email = ?
     WHERE id = ?`,
    [usuario.nombre, usuario.celular, usuario.email, usuario.id]
  );
  return result;
};

const buscarPorId = async (id) => {
  const [rows] = await pool.query(
    'SELECT id, nombre, user, celular, email, estado, rol FROM usuarios WHERE id = ?',
    [id]
  );
  return rows[0] || null;
};

const buscarPorUser = async (user) => {
  const [rows] = await pool.query(
    'SELECT * FROM usuarios WHERE user = ?',
    [user]
  );
  return rows[0] || null;
};

const inhabilitar = async (id) => {
  const [result] = await pool.query(
    `UPDATE usuarios SET estado = 'DESHABILITADO' WHERE id = ?`,
    [id]
  );
  return result;
};

const buscarTodos = async () => {
  const [rows] = await pool.query(
    'SELECT id, nombre, user, celular, email, estado, rol FROM usuarios'
  );
  return rows;
};

module.exports = { guardar, actualizar, buscarPorId, buscarPorUser, inhabilitar, buscarTodos };