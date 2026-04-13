import { useState } from "react";
import { getPatient } from "../api/patient.api";

function Patient() {
  const [doc, setDoc] = useState("");
  const [patient, setPatient] = useState(null);

  const handleSearch = async () => {
    const data = await getPatient(doc);
    setPatient(data);
  };

  return (
    <div className="p-6">
      <h1 className="text-xl font-bold">Buscar Paciente</h1>

      <input
        type="text"
        placeholder="Documento"
        className="border p-2 mr-2"
        onChange={(e) => setDoc(e.target.value)}
      />

      <button onClick={handleSearch} className="bg-blue-500 text-white p-2">
        Buscar
      </button>

      {patient && (
        <div className="mt-4">
          <p>Nombre: {patient.nombre}</p>
          <p>Documento: {patient.documento}</p>
        </div>
      )}
    </div>
  );
}

export default Patient;