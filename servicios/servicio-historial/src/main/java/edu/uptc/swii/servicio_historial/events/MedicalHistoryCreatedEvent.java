package edu.uptc.swii.servicio_historial.events;

import lombok.AllArgsConstructor;
import lombok.Data;

@Data
@AllArgsConstructor
public class MedicalHistoryCreatedEvent {
    private String historyId;
    private String patientId;
}