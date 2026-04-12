package edu.uptc.swii.servicio_historial.model;
import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;
import org.springframework.data.mongodb.core.mapping.Field;

@Document(collection = "eye_exams")
public class EyeExam {

    @Id
    private String id;
    private String medicalHistoryId;
    private String appointmentReason;
    private CorrectedVisualAcuity avccLE;
    private CorrectedVisualAcuity avccRE;
    private ExternalEyeExam externalEyeExamLE;
    private ExternalEyeExam externalEyeExamRE;
    private String behavior;
    private String observations;
}