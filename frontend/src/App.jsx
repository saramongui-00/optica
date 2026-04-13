import { useEffect, useState } from 'react';
import { getPacientes } from './services/pacientes';
import { getCitas } from './services/citas';

function App() {
  const [pacientes, setPacientes] = useState([]);
  const [citas, setCitas] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        setLoading(true);
        const [pacientesData, citasData] = await Promise.all([
          getPacientes(),
          getCitas()
        ]);
        setPacientes(pacientesData.data || []);
        setCitas(citasData.appointments || []);
        setError(null);
      } catch (err) {
        setError(err.detail || 'Error al cargar datos');
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, []);

  if (loading) {
    return (
      <div className="flex justify-center items-center h-screen">
        <div className="text-xl">Cargando datos...</div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="flex justify-center items-center h-screen">
        <div className="text-xl text-red-500">Error: {error}</div>
      </div>
    );
  }

  return (
    <div className="p-8">
      <h1 className="text-2xl font-bold mb-6">🏥 Óptica - Sistema de Gestión</h1>
      
      <div className="grid grid-cols-2 gap-6">
        {/* Pacientes */}
        <div className="border rounded-lg p-4">
          <h2 className="text-xl font-semibold mb-4">📋 Pacientes ({pacientes.length})</h2>
          <div className="space-y-2 max-h-96 overflow-y-auto">
            {pacientes.map(p => (
              <div key={p.id} className="border-b pb-2">
                <p className="font-medium">{p.nombres} {p.apellidos}</p>
                <p className="text-sm text-gray-600">Documento: {p.documento}</p>
              </div>
            ))}
          </div>
        </div>

        {/* Citas */}
        <div className="border rounded-lg p-4">
          <h2 className="text-xl font-semibold mb-4">📅 Citas ({citas.length})</h2>
          <div className="space-y-2 max-h-96 overflow-y-auto">
            {citas.map(c => (
              <div key={c.id} className="border-b pb-2">
                <p className="font-medium">Fecha: {c.date}</p>
                <p className="text-sm text-gray-600">Hora: {c.time}</p>
                <p className="text-sm">Paciente: {c.patient?.firstName} {c.patient?.lastName}</p>
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;