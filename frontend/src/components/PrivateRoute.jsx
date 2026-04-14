import { Navigate } from "react-router-dom";

function PrivateRoute({ children, rolesPermitidos }) {
  const token = localStorage.getItem("token");
  const rol = localStorage.getItem("rol");

  if (!token) {
    return <Navigate to="/" />;
  }

  if (rolesPermitidos && !rolesPermitidos.includes(rol)) {
    return <Navigate to="/user" />;
  }

  return children;
}

export default PrivateRoute;