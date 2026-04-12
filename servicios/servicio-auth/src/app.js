const express = require('express');
const eureka = require('./config/eureka');
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
  eureka.registrar();

  app.listen(process.env.PORT, () => {
    console.log(`ms-autenticacion corriendo en puerto ${process.env.PORT}`);
  });
};

iniciar();