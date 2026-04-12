package edu.uptc.swii.servicio_historial.model;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

@Getter
@Setter
@AllArgsConstructor
@NoArgsConstructor
public class Keratometry {
    private Eye eye;
    private double horizontal;
    private double vertical;
    private double axis;
    private String sights;
    private String astigmatism;


}
