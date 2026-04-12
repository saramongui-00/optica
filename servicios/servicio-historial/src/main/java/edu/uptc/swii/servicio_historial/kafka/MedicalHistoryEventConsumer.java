package edu.uptc.swii.servicio_historial.kafka;

import edu.uptc.swii.servicio_historial.events.PatientCreatedEvent;
import edu.uptc.swii.servicio_historial.service.MedicalHistoryService;
import lombok.RequiredArgsConstructor;
import org.springframework.kafka.annotation.KafkaListener;
import org.springframework.stereotype.Component;

@Component
@RequiredArgsConstructor
public class MedicalHistoryEventConsumer {

    private final MedicalHistoryService medicalHistoryService;

    @KafkaListener(topics = "patient.created", groupId = "historial-group")
    public void handlePatientCreated(PatientCreatedEvent event) {
        System.out.println("Evento recibido patient.created");
        medicalHistoryService.createMedicalHistory(event.getPatientId());
    }
}