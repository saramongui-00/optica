const { Kafka } = require('kafkajs');
const { fromJson } = require('../utils/jsonUtils');
const authService = require('./authService');

const kafka = new Kafka({
  clientId: 'ms-autenticacion-consumer',
  brokers: [process.env.KAFKA_BROKER || 'localhost:9092'],
});

const consumer = kafka.consumer({ groupId: 'auth_group' });

const conectar = async () => {
  await consumer.connect();
  await consumer.subscribe({ topic: 'login_events', fromBeginning: false });

  await consumer.run({
    eachMessage: async ({ topic, message }) => {
      const valor = message.value.toString();

      if (topic === 'login_events') {
        try {
          const { user, password } = fromJson(valor);
          const resultado = await authService.login(user, password);
          console.log('Login exitoso para:', user, '| rol:', resultado.rol);
        } catch (error) {
          console.error('Error procesando login_events:', error.message);
        }
      }
    },
  });

  console.log('Kafka consumer escuchando...');
};

module.exports = { conectar };