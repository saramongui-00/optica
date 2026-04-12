const express = require('express');
require('dotenv').config();
const authRoutes = require('./routes/authRoutes');
const producer = require('./service/authEventProducer');
const consumer = require('./service/authEventConsumer');

const app = express();
app.use(express.json());

app.use('/auth', authRoutes);

const iniciar = async () => {
  await producer.conectar();
  await consumer.conectar();

  app.listen(process.env.PORT, () => {
    console.log(`ms-autenticacion corriendo en puerto ${process.env.PORT}`);
  });
};

iniciar();