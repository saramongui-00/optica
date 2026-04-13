const bcrypt = require('bcryptjs');
const repository = require('../repository/usuarioRepository');

const guardar = async (usuario) => {
  const existe = await repository.buscarPorUser(usuario.user);
  if (existe) throw new Error('El nombre de usuario ya existe');

  const hash = await bcrypt.hash(usuario.password, 10);
  usuario.password = hash;
  return await repository.guardar(usuario);
};

const actualizar = async (usuario) => {
  const existe = await repository.buscarPorId(usuario.id);
  if (!existe) throw new Error('Usuario no encontrado');
  return await repository.actualizar(usuario);
};

const buscarPorId = async (id) => {
  const usuario = await repository.buscarPorId(id);
  if (!usuario) throw new Error('Usuario no encontrado');
  return usuario;
};

const buscarTodos = async () => {
  return await repository.buscarTodos();
};

const inhabilitar = async (id) => {
  const existe = await repository.buscarPorId(id);
  if (!existe) throw new Error('Usuario no encontrado');
  return await repository.inhabilitar(id);
};

module.exports = { guardar, actualizar, buscarPorId, buscarTodos, inhabilitar };