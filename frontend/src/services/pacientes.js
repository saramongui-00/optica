import { pacientesAPI } from './api';

export const getPacientes = async () => {
  const response = await pacientesAPI.get('/pacientes/');
  return response.data;
};

export const getPacienteById = async (id) => {
  const response = await pacientesAPI.get(`/pacientes/${id}`);
  return response.data;
};

export const getPacienteByDocumento = async (documento) => {
  const response = await pacientesAPI.get(`/pacientes/documento/${documento}`);
  return response.data;
};

export const createPaciente = async (data) => {
  const response = await pacientesAPI.post('/pacientes/', data);
  return response.data;
};

export const updatePaciente = async (id, data) => {
  const response = await pacientesAPI.put(`/pacientes/${id}`, data);
  return response.data;
};

export const deletePaciente = async (id) => {
  const response = await pacientesAPI.delete(`/pacientes/${id}`);
  return response.data;
};

export const getSexos = async () => {
  const response = await pacientesAPI.get('/pacientes/enums/sexo');
  return response.data;
};

export const getEstadosCiviles = async () => {
  const response = await pacientesAPI.get('/pacientes/enums/estado-civil');
  return response.data;
};