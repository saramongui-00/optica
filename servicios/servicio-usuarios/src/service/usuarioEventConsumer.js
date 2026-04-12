const { Kafka } = require('kafkajs');
const { fromJson } = require('../utils/jsonUtils');
const usuarioService = require('./usuarioService');

const kafka = new Kafka({
  clientId: 'ms-usuarios-consumer',
  brokers: [process.env.KAFKA_BROKER || 'localhost:9092'],
});

const consumer = kafka.consumer({ groupId: 'usuario_group' });

const conectar = async () => {
  await consumer.connect();

  await consumer.subscribe({ topic: 'adduser_events', fromBeginning: false });
  await consumer.subscribe({ topic: 'edituser_events', fromBeginning: false });
  await consumer.subscribe({ topic: 'finduser_events', fromBeginning: false });
  await consumer.subscribe({ topic: 'disableuser_events', fromBeginning: false });

  await consumer.run({
    eachMessage: async ({ topic, message }) => {
      const valor = message.value.toString();

     if (topic === 'adduser_events') {
  try {
    const usuario = fromJson(valor);
    usuario.estado = 'HABILITADO';
    await usuarioService.guardar(usuario);
    console.log('Usuario creado:', usuario.user);
  } catch (error) {
    console.error('Error procesando adduser_events:', error.message);
  }
}

if (topic === 'edituser_events') {
  try {
    const usuario = fromJson(valor);
    await usuarioService.actualizar(usuario);
    console.log('Usuario actualizado:', usuario.id);
  } catch (error) {
    console.error('Error procesando edituser_events:', error.message);
  }
}

if (topic === 'finduser_events') {
  try {
    const usuario = await usuarioService.buscarPorId(valor);
    console.log('Usuario encontrado:', usuario);
  } catch (error) {
    console.error('Error procesando finduser_events:', error.message);
  }
}

if (topic === 'disableuser_events') {
  try {
    await usuarioService.inhabilitar(valor);
    console.log('Usuario inhabilitado:', valor);
  } catch (error) {
    console.error('Error procesando disableuser_events:', error.message);
  }
}
    },
  });

  console.log('Kafka consumer escuchando...');
};

module.exports = { conectar };