package edu.uptc.swii.servicio_historial.model;
import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;
import org.springframework.data.mongodb.core.mapping.Field;
@Getter
@Setter
@AllArgsConstructor
@NoArgsConstructor
public class ExternalEyeExam {

    private Eye eye;
    private String pupil;
    private String conjunctiva;
    private String cristallineLens;
    private String anteriorChamber;
    private String eyelids;
    private String cornea;
    private String lacrimalPuncta;
    private String iris;
}
