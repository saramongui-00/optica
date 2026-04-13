const pool = require('../config/db');

const buscarPorUser = async (user) => {
  const [rows] = await pool.query(
    'SELECT * FROM usuarios WHERE user = ? AND estado = "HABILITADO"',
    [user]
  );
  return rows[0] || null;
};

module.exports = { buscarPorUser };