package edu.uptc.swii.servicio_historial.model;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

import java.time.LocalDate;
@Getter
@Setter
@AllArgsConstructor
@NoArgsConstructor
public class PersonalBackground {
    private String personalBackground;
    private String familiarBackground;
    private LocalDate wearGlassesSince;
    private String medications;
    private String observations;
}
