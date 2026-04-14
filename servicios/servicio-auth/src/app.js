const express = require('express');
const cors = require('cors');
const eureka = require('./config/eureka');
require('dotenv').config();
const authRoutes = require('./routes/authRoutes');
const producer = require('./service/authEventProducer');
const consumer = require('./service/authEventConsumer');

const app = express();

app.use(cors({
  origin: 'http://localhost:5173',
  methods: ['GET', 'POST', 'PUT', 'PATCH', 'DELETE'],
  allowedHeaders: ['Content-Type', 'Authorization'],
}));

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