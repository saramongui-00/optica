const { Eureka } = require('eureka-js-client');

const client = new Eureka({
  instance: {
    app: 'ms-autenticacion',
    hostName: 'localhost',
    ipAddr: '127.0.0.1',
    port: {
      '$': 8081,
      '@enabled': true,
    },
    vipAddress: 'ms-autenticacion',
    dataCenterInfo: {
      '@class': 'com.netflix.appinfo.InstanceInfo$DefaultDataCenterInfo',
      name: 'MyOwn',
    },
  },
  eureka: {
    host: 'localhost',
    port: 8761,
    servicePath: '/eureka/apps/',
  },
});

const registrar = () => {
  client.start((error) => {
    if (error) {
      console.error('Error registrando en Eureka:', error);
    } else {
      console.log('ms-autenticacion registrado en Eureka');
    }
  });
};

module.exports = { registrar };