package edu.uptc.swii.servicio_historial.kafka;

import edu.uptc.swii.servicio_historial.events.EyeExamCreatedEvent;
import lombok.RequiredArgsConstructor;
import org.springframework.kafka.core.KafkaTemplate;
import org.springframework.stereotype.Component;

@Component
@RequiredArgsConstructor
public class EyeExamEventProducer {
    private static final String TOPIC_EYE_EXAM_CREATED = "eye-exam.created";

    private final KafkaTemplate<String, Object> kafkaTemplate;

    public void publishEyeExamCreated(String examId, String historyId) {
        EyeExamCreatedEvent event =
                new EyeExamCreatedEvent(examId, historyId);

        kafkaTemplate.send(TOPIC_EYE_EXAM_CREATED, event);
    }
}