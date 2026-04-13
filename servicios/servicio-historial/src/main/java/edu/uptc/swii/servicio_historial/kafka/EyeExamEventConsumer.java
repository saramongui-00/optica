package edu.uptc.swii.servicio_historial.kafka;

import edu.uptc.swii.servicio_historial.events.AppointmentCompletedEvent;
import edu.uptc.swii.servicio_historial.service.EyeExamService;
import lombok.RequiredArgsConstructor;
import org.springframework.kafka.annotation.KafkaListener;
import org.springframework.stereotype.Component;

@Component
@RequiredArgsConstructor
public class EyeExamEventConsumer {

    private final EyeExamService eyeExamService;

    @KafkaListener(topics = "appointment.completed", groupId = "historial-group")
    public void handleAppointmentCompleted(AppointmentCompletedEvent event) {
        System.out.println("Evento recibido appointment.completed");
        eyeExamService.prepareEyeExam(event.getPatientId(), event.getAppointmentId());
    }
}