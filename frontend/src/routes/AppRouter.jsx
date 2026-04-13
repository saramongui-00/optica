import { BrowserRouter, Routes, Route } from "react-router-dom";
import Login from "../pages/Login";
import User from "../pages/User";
import Patient from "../pages/Patient";

function AppRouter() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Login />} />
        <Route path="/user" element={<User />} />
        <Route path="/patient" element={<Patient />} />
      </Routes>
    </BrowserRouter>
  );
}

export default AppRouter;