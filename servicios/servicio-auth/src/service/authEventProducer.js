const { Kafka } = require('kafkajs');
const { toJson } = require('../utils/jsonUtils');

const kafka = new Kafka({
  clientId: 'ms-autenticacion',
  brokers: [process.env.KAFKA_BROKER || 'localhost:9092'],
});

const producer = kafka.producer();

const conectar = async () => {
  await producer.connect();
  console.log('Kafka producer conectado');
};

const sendLoginEvent = async (datos) => {
  await producer.send({
    topic: 'login_events',
    messages: [{ value: toJson(datos) }],
  });
};

module.exports = { conectar, sendLoginEvent };