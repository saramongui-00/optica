const express = require('express');
const router = express.Router();
const { login, validarToken } = require('../controller/authController');

router.post('/login', login);
router.post('/validate', validarToken);

module.exports = router;