const express = require('express');
const router = express.Router();
const {
  registrarUsuario,
  consultarUsuario,
  modificarUsuario,
  inhabilitarUsuario,
  buscarTodos
} = require('../controller/usuarioController');

const { verificarToken, soloOptometra } = require('../middleware/authMiddleware');

router.get('/', verificarToken, buscarTodos);
router.get('/:id', verificarToken, consultarUsuario);
router.post('/', verificarToken, soloOptometra, registrarUsuario);
router.put('/:id', verificarToken, soloOptometra, modificarUsuario);
router.patch('/:id/inhabilitar', verificarToken, soloOptometra, inhabilitarUsuario);

module.exports = router;