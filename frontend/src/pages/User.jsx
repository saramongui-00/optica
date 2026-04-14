import { useEffect, useState } from "react";
import { getUser } from "../api/user.api";
import { useNavigate } from "react-router-dom";

function User() {
  const [user, setUser] = useState(null);
  const navigate = useNavigate();

  useEffect(() => {
    const token = localStorage.getItem("token");
    if (token) {
      const payload = JSON.parse(atob(token.split('.')[1]));
      getUser(payload.id).then(setUser);
    }
  }, []);

  const handleLogout = () => {
    localStorage.clear();
    navigate("/");
  };

  if (!user) return (
    <div style={{
      minHeight: "100vh", display: "flex",
      alignItems: "center", justifyContent: "center",
      fontFamily: "'DM Sans', sans-serif", background: "#f0f4f8",
    }}>
      <div style={{ color: "#64748b" }}>Cargando...</div>
    </div>
  );

  return (
    <div style={{
      minHeight: "100vh", background: "#f0f4f8",
      fontFamily: "'DM Sans', sans-serif",
    }}>
      <link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@300;400;500;600&family=Playfair+Display:wght@600&display=swap" rel="stylesheet" />

      <nav style={{
        background: "#0a2540", padding: "0 40px",
        height: "60px", display: "flex",
        alignItems: "center", justifyContent: "space-between",
      }}>
        <span style={{
          fontFamily: "'Playfair Display', serif",
          color: "white", fontSize: "18px",
        }}>
          Óptica ISIS
        </span>
        <div style={{ display: "flex", alignItems: "center", gap: "20px" }}>
          <span style={{ color: "rgba(255,255,255,0.6)", fontSize: "14px" }}>
            {user.nombre}
          </span>
          <button
            onClick={handleLogout}
            style={{
              background: "rgba(255,255,255,0.1)",
              border: "1px solid rgba(255,255,255,0.2)",
              color: "white", padding: "6px 16px",
              borderRadius: "6px", fontSize: "13px",
              cursor: "pointer",
            }}
          >
            Cerrar sesión
          </button>
        </div>
      </nav>

      <div style={{ padding: "40px" }}>
        <h1 style={{
          fontFamily: "'Playfair Display', serif",
          color: "#0a2540", fontSize: "26px",
          marginBottom: "24px",
        }}>
          Perfil de usuario
        </h1>

        <div style={{
          background: "white", borderRadius: "14px",
          padding: "28px", maxWidth: "500px",
          boxShadow: "0 1px 3px rgba(0,0,0,0.06)",
        }}>
          <div style={{
            width: "56px", height: "56px", borderRadius: "50%",
            background: "#0a2540", display: "flex",
            alignItems: "center", justifyContent: "center",
            color: "white", fontSize: "20px", fontWeight: 600,
            marginBottom: "20px",
          }}>
            {user.nombre?.charAt(0).toUpperCase()}
          </div>

          {[
            ["Nombre", user.nombre],
            ["Usuario", user.user],
            ["Email", user.email],
            ["Celular", user.celular],
            ["Rol", user.rol],
            ["Estado", user.estado],
          ].map(([label, value]) => (
            <div key={label} style={{
              display: "flex", justifyContent: "space-between",
              padding: "12px 0",
              borderBottom: "1px solid #f1f5f9",
            }}>
              <span style={{ color: "#64748b", fontSize: "14px" }}>{label}</span>
              <span style={{
                color: label === "Rol" ? "#0d5c8f" : "#0a2540",
                fontSize: "14px", fontWeight: 500,
              }}>
                {value}
              </span>
            </div>
          ))}
        </div>

        <div style={{ marginTop: "28px", display: "flex", gap: "12px" }}>
          <button
            onClick={() => navigate("/patient")}
            style={{
              background: "#0a2540", color: "white",
              border: "none", padding: "11px 24px",
              borderRadius: "8px", fontSize: "14px",
              cursor: "pointer", fontFamily: "'DM Sans', sans-serif",
            }}
          >
            Ver pacientes
          </button>
        </div>
      </div>
    </div>
  );
}

export default User;