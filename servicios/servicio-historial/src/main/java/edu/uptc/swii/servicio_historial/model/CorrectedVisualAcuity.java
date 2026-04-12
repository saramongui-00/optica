package edu.uptc.swii.servicio_historial.model;

import org.springframework.data.mongodb.core.mapping.Field;

public class CorrectedVisualAcuity {

    private Eye eye;
    private String closeupVision;
    private String distantVision;
    private String tool;
    private String observations;
}
