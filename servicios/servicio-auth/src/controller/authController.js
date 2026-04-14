const authService = require('../service/authService');
const producer = require('../service/authEventProducer');

const login = async (req, res) => {
  try {
    const { user, password } = req.body;

    if (!user || !password) {
      return res.status(400).json({ mensaje: 'Usuario y contraseña requeridos' });
    }

    await producer.sendLoginEvent({ user, password });
    const resultado = await authService.login(user, password);
    res.json(resultado);

  } catch (error) {
    res.status(401).json({ mensaje: error.message });
  }
};

const validarToken = (req, res) => {
  try {
    const { token } = req.body;
    if (!token) return res.status(400).json({ mensaje: 'Token requerido' });

    const decoded = authService.validarToken(token);
    res.json({ valido: true, usuario: decoded });
  } catch (error) {
    res.status(401).json({ valido: false, mensaje: 'Token inválido o expirado' });
  }
};

const logout = async (req, res) => {
  try {
    const { user } = req.body;
    await producer.sendLogoutEvent({ user });
    res.json({ mensaje: 'Sesión cerrada exitosamente' });
  } catch (error) {
    res.status(500).json({ mensaje: error.message });
  }
};

module.exports = { login, validarToken, logout };