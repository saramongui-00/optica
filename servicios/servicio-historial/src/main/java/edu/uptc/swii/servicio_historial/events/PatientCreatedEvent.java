package edu.uptc.swii.servicio_historial.events;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@NoArgsConstructor
@AllArgsConstructor
public class PatientCreatedEvent {
    private String patientId;
}