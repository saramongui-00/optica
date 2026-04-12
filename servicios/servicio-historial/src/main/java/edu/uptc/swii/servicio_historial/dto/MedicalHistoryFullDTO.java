package edu.uptc.swii.servicio_historial.dto;

import edu.uptc.swii.servicio_historial.model.EyeExam;
import edu.uptc.swii.servicio_historial.model.MedicalHistory;
import lombok.AllArgsConstructor;
import lombok.Data;

import java.util.List;

@Data
@AllArgsConstructor
public class MedicalHistoryFullDTO {
    private MedicalHistory medicalHistory;
    private List<EyeExam> exams;
}