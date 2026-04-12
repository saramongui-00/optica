package edu.uptc.swii.servicio_historial.model;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

@Getter
@Setter
@AllArgsConstructor
@NoArgsConstructor
public class UncorrectedVisualAcuity {
    private Eye eye;
    private String closeupVision;
    private String distantVision;
    private String tool;
    private String observations;
}
