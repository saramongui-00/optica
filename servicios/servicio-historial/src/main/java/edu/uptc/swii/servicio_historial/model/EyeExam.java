package edu.uptc.swii.servicio_historial.model;
import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;
import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;
import org.springframework.data.mongodb.core.mapping.Field;

@Getter
@Setter
@AllArgsConstructor
@NoArgsConstructor
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