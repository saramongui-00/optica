import { userAPI } from "../utils/axios";

export const getUser = async (id) => {
  const res = await userAPI.get(`/usuarios/${id}`);
  return res.data;
};