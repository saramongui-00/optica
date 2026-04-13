const { Eureka } = require('eureka-js-client');

const client = new Eureka({
  instance: {
    app: 'ms-usuarios',
    hostName: 'localhost',
    ipAddr: '127.0.0.1',
    port: {
      '$': 8082,
      '@enabled': true,
    },
    vipAddress: 'ms-usuarios',
    dataCenterInfo: {
      '@class': 'com.netflix.appinfo.InstanceInfo$DefaultDataCenterInfo',
      name: 'MyOwn',
    },
  },
  eureka: {
    host: process.env.EUREKA_HOST || 'localhost',
    port: 8761,
    servicePath: '/eureka/apps/',
  },
});

const registrar = () => {
  client.start((error) => {
    if (error) {
      console.error('Error registrando en Eureka:', error);
    } else {
      console.log('ms-usuarios registrado en Eureka');
    }
  });
};

module.exports = { registrar };