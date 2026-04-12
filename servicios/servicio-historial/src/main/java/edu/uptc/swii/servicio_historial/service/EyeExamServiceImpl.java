package edu.uptc.swii.servicio_historial.service;

import edu.uptc.swii.servicio_historial.model.EyeExam;
import edu.uptc.swii.servicio_historial.repository.EyeExamRepository;
import edu.uptc.swii.servicio_historial.repository.MedicalHistoryRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
@RequiredArgsConstructor
public class EyeExamServiceImpl implements EyeExamService {

    private final EyeExamRepository examRepository;
    private final MedicalHistoryRepository historyRepository;

    @Override
    public EyeExam createExam(String medicalHistoryId, EyeExam exam) {
        historyRepository.findById(medicalHistoryId)
                .orElseThrow(() -> new RuntimeException("Historial no existe"));

        exam.setMedicalHistoryId(medicalHistoryId);

        return examRepository.save(exam);
    }

    @Override
    public EyeExam getExam(String examId) {
        return examRepository.findById(examId)
                .orElseThrow(() -> new RuntimeException("Examen no encontrado"));
    }

    @Override
    public List<EyeExam> getExamsByHistory(String medicalHistoryId) {
        return examRepository.findByMedicalHistoryId(medicalHistoryId);
    }
}