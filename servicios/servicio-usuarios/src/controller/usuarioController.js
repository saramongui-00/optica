const producer = require('../service/usuarioEventProducer');
const usuarioService = require('../service/usuarioService');

const registrarUsuario = async (req, res) => {
  try {
    const usuario = req.body;
    await producer.sendAddUsuarioEvent(usuario);
    res.status(202).json({ mensaje: 'Evento de creación enviado' });
  } catch (error) {
    res.status(500).json({ mensaje: error.message });
  }
};

const consultarUsuario = async (req, res) => {
  try {
    const { id } = req.params;
    const usuario = await usuarioService.buscarPorId(id);
    res.json(usuario);
  } catch (error) {
    res.status(404).json({ mensaje: error.message });
  }
};

const modificarUsuario = async (req, res) => {
  try {
    const usuario = { ...req.body, id: req.params.id };
    await producer.sendEditUsuarioEvent(usuario);
    res.status(202).json({ mensaje: 'Evento de modificación enviado' });
  } catch (error) {
    res.status(500).json({ mensaje: error.message });
  }
};

const inhabilitarUsuario = async (req, res) => {
  try {
    const { id } = req.params;
    await producer.sendInhabilitarUsuarioEvent(id);
    res.status(202).json({ mensaje: 'Evento de inhabilitación enviado' });
  } catch (error) {
    res.status(500).json({ mensaje: error.message });
  }
};

const buscarTodos = async (req, res) => {
  try {
    const usuarios = await usuarioService.buscarTodos();
    res.json(usuarios);
  } catch (error) {
    res.status(500).json({ mensaje: error.message });
  }
};

module.exports = {
  registrarUsuario,
  consultarUsuario,
  modificarUsuario,
  inhabilitarUsuario,
  buscarTodos
};