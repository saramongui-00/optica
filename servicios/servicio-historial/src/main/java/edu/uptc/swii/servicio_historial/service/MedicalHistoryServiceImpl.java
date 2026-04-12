package edu.uptc.swii.servicio_historial.service;

import edu.uptc.swii.servicio_historial.dto.MedicalHistoryFullDTO;
import edu.uptc.swii.servicio_historial.model.EyeExam;
import edu.uptc.swii.servicio_historial.model.MedicalHistory;
import edu.uptc.swii.servicio_historial.repository.EyeExamRepository;
import edu.uptc.swii.servicio_historial.repository.MedicalHistoryRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
@RequiredArgsConstructor
public class MedicalHistoryServiceImpl implements MedicalHistoryService {

    private final MedicalHistoryRepository historyRepository;
    private final EyeExamRepository examRepository;

    @Override
    public MedicalHistory createMedicalHistory(String patientId) {

        // evitar duplicados (1 historial por paciente)
        historyRepository.findByPatientId(patientId)
                .ifPresent(h -> {
                    throw new RuntimeException("El paciente ya tiene historial");
                });

        MedicalHistory history = new MedicalHistory();
        history.setPatientId(patientId);

        return historyRepository.save(history);
    }

    @Override
    public MedicalHistory getById(String id) {
        return historyRepository.findById(id)
                .orElseThrow(() -> new RuntimeException("Historial no encontrado"));
    }

    @Override
    public MedicalHistory getByPatientId(String patientId) {
        return historyRepository.findByPatientId(patientId)
                .orElseThrow(() -> new RuntimeException("Historial no encontrado"));
    }

    @Override
    public MedicalHistoryFullDTO getFullHistory(String patientId) {

        MedicalHistory history = getByPatientId(patientId);
        List<EyeExam> exams = examRepository.findByMedicalHistoryId(history.getId());

        return new MedicalHistoryFullDTO(history, exams);
    }
}
