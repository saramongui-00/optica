import { useState, useEffect } from 'react';
import { getPacientes, createPaciente, deletePaciente } from '../services/pacientes';

export const usePacientes = () => {
  const [pacientes, setPacientes] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  const fetchPacientes = async () => {
    try {
      setLoading(true);
      const data = await getPacientes();
      setPacientes(data.data || []);
      setError(null);
    } catch (err) {
      setError(err.detail || 'Error al cargar pacientes');
    } finally {
      setLoading(false);
    }
  };

  const addPaciente = async (pacienteData) => {
    try {
      const result = await createPaciente(pacienteData);
      await fetchPacientes();
      return result;
    } catch (err) {
      throw err;
    }
  };

  const removePaciente = async (id) => {
    try {
      await deletePaciente(id);
      await fetchPacientes();
    } catch (err) {
      throw err;
    }
  };

  useEffect(() => {
    fetchPacientes();
  }, []);

  return { pacientes, loading, error, addPaciente, removePaciente, fetchPacientes };
};