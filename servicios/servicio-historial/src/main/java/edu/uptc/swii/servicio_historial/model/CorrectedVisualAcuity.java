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
public class CorrectedVisualAcuity {

    private Eye eye;
    private String closeupVision;
    private String distantVision;
    private String tool;
    private String observations;
}
