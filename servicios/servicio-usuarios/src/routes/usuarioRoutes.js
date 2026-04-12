const express = require('express');
const router = express.Router();
const {
  registrarUsuario,
  consultarUsuario,
  modificarUsuario,
  inhabilitarUsuario,
  buscarTodos
} = require('../controller/UsuarioController');

router.get('/', buscarTodos);
router.post('/', registrarUsuario);
router.get('/:id', consultarUsuario);
router.put('/:id', modificarUsuario);
router.patch('/:id/inhabilitar', inhabilitarUsuario);

module.exports = router;