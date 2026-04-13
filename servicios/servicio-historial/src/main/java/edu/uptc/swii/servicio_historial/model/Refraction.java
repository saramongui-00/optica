package edu.uptc.swii.servicio_historial.model;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

@Getter
@Setter
@AllArgsConstructor
@NoArgsConstructor
public class Refraction {
    private Eye eye;
    private double reHorizontal;
    private double reVertical;
    private double reAxis;
    private double rdHorizontal;
    private double rdVertical;
    private double rdAxis;
    private double subHorizontal;
    private double subVertical;
    private double subAxis;
}
