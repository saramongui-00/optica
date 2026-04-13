import { useEffect, useState } from "react";
import { getUser } from "../api/user.api";

function User() {
  const [user, setUser] = useState(null);

  useEffect(() => {
    getUser(1).then(setUser); // luego lo hacemos dinámico
  }, []);

  if (!user) return <p>Cargando...</p>;

  return (
    <div className="p-6">
      <h1 className="text-xl font-bold">Usuario</h1>
      <p>Nombre: {user.nombre}</p>
      <p>Email: {user.email}</p>
      <p>Rol: {user.rol}</p>
    </div>
  );
}

export default User;