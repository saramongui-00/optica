import { authAPI } from "../utils/axios";

export const loginRequest = async (data) => {
  const res = await authAPI.post("/login", data);
  return res.data;
};