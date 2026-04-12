package edu.uptc.swii.servicio_historial.kafka;

import edu.uptc.swii.servicio_historial.events.MedicalHistoryCreatedEvent;
import lombok.RequiredArgsConstructor;
import org.springframework.kafka.core.KafkaTemplate;
import org.springframework.stereotype.Component;
@Component
@RequiredArgsConstructor
public class MedicalHistoryEventProducer {
    private static final String TOPIC_MEDICALH_CREATED = "medical-history.created";
    private final KafkaTemplate<String, Object> kafkaTemplate;

    public void publishMedicalHistoryCreated(String historyId, String patientId) {
        MedicalHistoryCreatedEvent event =
                new MedicalHistoryCreatedEvent(historyId, patientId);

        kafkaTemplate.send(TOPIC_MEDICALH_CREATED, event);
    }
}