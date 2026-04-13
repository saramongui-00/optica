package edu.uptc.swii.servicio_historial.service;

import edu.uptc.swii.servicio_historial.model.EyeExam;

import java.util.List;

public interface EyeExamService {

    EyeExam createExam(String medicalHistoryId, EyeExam exam);

    EyeExam getExam(String examId);

    List<EyeExam> getExamsByHistory(String medicalHistoryId);

    void prepareEyeExam(String patientId, String appointmentId);
}