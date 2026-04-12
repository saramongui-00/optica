package edu.uptc.swii.servicio_historial.events;

import lombok.AllArgsConstructor;
import lombok.Data;

@   Data
@AllArgsConstructor
public class EyeExamCreatedEvent {
    private String examId;
    private String historyId;
}