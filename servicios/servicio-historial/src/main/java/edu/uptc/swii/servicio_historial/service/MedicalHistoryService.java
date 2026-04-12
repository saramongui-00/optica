package edu.uptc.swii.servicio_historial.service;

import edu.uptc.swii.servicio_historial.dto.MedicalHistoryFullDTO;
import edu.uptc.swii.servicio_historial.model.MedicalHistory;

public interface MedicalHistoryService {

    MedicalHistory createMedicalHistory(String patientId);

    MedicalHistory getById(String id);

    MedicalHistory getByPatientId(String patientId);

    MedicalHistoryFullDTO getFullHistory(String patientId);
}