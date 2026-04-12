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
        const usuario = fromJson(valor);
        await usuarioService.guardar(usuario);
        console.log('Usuario creado:', usuario.user);
      }

      if (topic === 'edituser_events') {
        const usuario = fromJson(valor);
        await usuarioService.actualizar(usuario);
        console.log('Usuario actualizado:', usuario.id);
      }

      if (topic === 'finduser_events') {
        const usuario = await usuarioService.buscarPorId(valor);
        console.log('Usuario encontrado:', usuario);
      }

      if (topic === 'disableuser_events') {
        await usuarioService.inhabilitar(valor);
        console.log('Usuario inhabilitado:', valor);
      }
    },
  });

  console.log('Kafka consumer escuchando...');
};

module.exports = { conectar };