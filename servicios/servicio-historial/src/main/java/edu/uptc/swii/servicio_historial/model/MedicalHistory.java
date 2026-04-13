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
@Document(collection = "medical_history")
public class MedicalHistory {

    @Id
    private String id;

    @Field("patient_id")
    private String patientId;

    @Field("personal_background")
    private PersonalBackground personalBackground;
}