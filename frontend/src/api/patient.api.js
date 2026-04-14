import { patientAPI } from "../utils/axios";

export const getPatient = async (documento) => {
  const res = await patientAPI.get(`/pacientes/documento/${documento}`);
  return res.data;
};