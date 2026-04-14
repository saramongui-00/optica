const bcrypt = require('bcryptjs');
const jwt = require('jsonwebtoken');
const repository = require('../repository/authRepository');

const login = async (user, password) => {
  const usuario = await repository.buscarPorUser(user);

  if (!usuario) throw new Error('Credenciales inválidas');

  const passwordValida = await bcrypt.compare(password, usuario.password);
  
  if (!passwordValida) throw new Error('Credenciales inválidas');

  const token = jwt.sign(
    {
      id: usuario.id,
      user: usuario.user,
      rol: usuario.rol
    },
    process.env.JWT_SECRET
   // { expiresIn: process.env.JWT_EXPIRES_IN }
  );
  console.log("Token generado:", token);

  return { token, rol: usuario.rol, nombre: usuario.nombre };
};

const validarToken = (token) => {
  const decoded = jwt.verify(token, process.env.JWT_SECRET);
  return decoded;
};

module.exports = { login, validarToken };