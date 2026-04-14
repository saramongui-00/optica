import { useState } from "react";
import { loginRequest } from "../api/auth.api";
import { useAuth } from "../hooks/useAuth";
import { useNavigate } from "react-router-dom";

function Login() {
  const [form, setForm] = useState({ user: "", password: "" });
  const [error, setError] = useState("");
  const { login } = useAuth();
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const data = await loginRequest(form);
      login(data);
      navigate("/user");
    } catch (err) {
      setError("Credenciales inválidas");
    }
  };

  return (
    <div className="flex h-screen items-center justify-center bg-gray-100">
      <form
        onSubmit={handleSubmit}
        className="bg-white p-6 rounded-xl shadow-md w-80"
      >
        <h2 className="text-2xl font-bold mb-4">Login</h2>

        <input
          type="text"
          placeholder="Usuario"
          className="w-full mb-3 p-2 border rounded"
          onChange={(e) =>
            setForm({ ...form, user: e.target.value })
          }
        />

        <input
          type="password"
          placeholder="Contraseña"
          className="w-full mb-3 p-2 border rounded"
          onChange={(e) =>
            setForm({ ...form, password: e.target.value })
          }
        />

        {error && <p className="text-red-500">{error}</p>}

        <button className="w-full bg-blue-500 text-white p-2 rounded">
          Ingresar
        </button>
      </form>
    </div>
  );
}

export default Login;