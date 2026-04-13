import axios from 'axios';

// Usar 127.0.0.1 en lugar de localhost (más confiable)
export const pacientesAPI = axios.create({
  baseURL: 'http://127.0.0.1:8084',
  timeout: 10000,
});

export const citasAPI = axios.create({
  baseURL: 'http://127.0.0.1:8083',
  timeout: 10000,
});

export const authAPI = axios.create({
  baseURL: 'http://127.0.0.1:8082',
  timeout: 10000,
});

// Interceptor para manejar errores
const handleError = (error) => {
  if (error.response) {
    console.error('Error response:', error.response.data);
    return Promise.reject(error.response.data);
  }
  if (error.request) {
    console.error('No response from server:', error.request);
    return Promise.reject({ detail: 'No se pudo conectar con el servidor' });
  }
  console.error('Error:', error.message);
  return Promise.reject({ detail: error.message });
};

pacientesAPI.interceptors.response.use(response => response, handleError);
citasAPI.interceptors.response.use(response => response, handleError);
authAPI.interceptors.response.use(response => response, handleError);