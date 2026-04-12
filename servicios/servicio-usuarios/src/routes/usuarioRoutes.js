const express = require('express');
const router = express.Router();
const {
  registrarUsuario,
  consultarUsuario,
  modificarUsuario,
  inhabilitarUsuario
} = require('../controller/usuarioController');

router.post('/', registrarUsuario);
router.get('/:id', consultarUsuario);
router.put('/:id', modificarUsuario);
router.patch('/:id/inhabilitar', inhabilitarUsuario);

module.exports = router;