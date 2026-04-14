const express = require('express');
const router = express.Router();
const { login, validarToken, logout} = require('../controller/authController');

router.post('/login', login);
router.post('/validate', validarToken);
router.post('/logout', logout);

module.exports = router;