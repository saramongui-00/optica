const express = require('express');
const cors = require('cors');
const eureka = require('./config/eureka');
require('dotenv').config();
const usuarioRoutes = require('./routes/usuarioRoutes');
const producer = require('./service/usuarioEventProducer');
const consumer = require('./service/usuarioEventConsumer');

const app = express();

app.use(cors({
  origin: 'http://localhost:5173',
  methods: ['GET', 'POST', 'PUT', 'PATCH', 'DELETE'],
  allowedHeaders: ['Content-Type', 'Authorization'],
}));

app.use(express.json());

app.use('/usuarios', usuarioRoutes);

const iniciar = async () => {
  await producer.conectar();
  await consumer.conectar();
  eureka.registrar();

  app.listen(process.env.PORT, () => {
    console.log(`ms-usuarios corriendo en puerto ${process.env.PORT}`);
  });
};

iniciar();