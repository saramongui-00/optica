import { citasAPI } from './api';

export const getCitas = async (page = 1, limit = 10) => {
  const response = await citasAPI.get(`/appointments/?page=${page}&limit=${limit}`);
  return response.data;
};

export const getCitaById = async (id) => {
  const response = await citasAPI.get(`/appointments/${id}`);
  return response.data;
};

export const getCitasByDate = async (date) => {
  const response = await citasAPI.get(`/appointments/date/${date}`);
  return response.data;
};

export const getCitasByPatientDocument = async (document) => {
  const response = await citasAPI.get(`/appointments/patient/${document}`);
  return response.data;
};

export const createCita = async (data) => {
  const response = await citasAPI.post('/appointments/', data);
  return response.data;
};

export const cancelCita = async (id) => {
  const response = await citasAPI.put(`/appointments/${id}/cancel`);
  return response.data;
};

export const updateCita = async (id, data) => {
  const response = await citasAPI.put(`/appointments/${id}`, data);
  return response.data;
};

export const getEstadosCita = async () => {
  const response = await citasAPI.get('/appointments/enums/states');
  return response.data;
};