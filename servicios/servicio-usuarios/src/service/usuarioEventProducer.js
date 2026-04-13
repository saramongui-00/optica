const { Kafka } = require('kafkajs');
const { toJson } = require('../utils/jsonUtils');

const kafka = new Kafka({
  clientId: 'ms-usuarios',
  brokers: [process.env.KAFKA_BROKER || 'localhost:9092'],
});

const producer = kafka.producer();

const conectar = async () => {
  await producer.connect();
  console.log('Kafka producer conectado');
};

const sendAddUsuarioEvent = async (usuario) => {
  await producer.send({
    topic: 'adduser_events',
    messages: [{ value: toJson(usuario) }],
  });
};

const sendEditUsuarioEvent = async (usuario) => {
  await producer.send({
    topic: 'edituser_events',
    messages: [{ value: toJson(usuario) }],
  });
};

const sendFindUsuarioEvent = async (id) => {
  await producer.send({
    topic: 'finduser_events',
    messages: [{ value: String(id) }],
  });
};

const sendInhabilitarUsuarioEvent = async (id) => {
  await producer.send({
    topic: 'disableuser_events',
    messages: [{ value: String(id) }],
  });
};

module.exports = {
  conectar,
  sendAddUsuarioEvent,
  sendEditUsuarioEvent,
  sendFindUsuarioEvent,
  sendInhabilitarUsuarioEvent,
};