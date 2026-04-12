package edu.uptc.swii.servicio_historial.controller;

import edu.uptc.swii.servicio_historial.model.EyeExam;
import edu.uptc.swii.servicio_historial.service.EyeExamService;
import lombok.RequiredArgsConstructor;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/historial")
@RequiredArgsConstructor
public class EyeExamController {

    private final EyeExamService examService;

    // Crear examen para un historial
    @PostMapping("/{historyId}/examen")
    public ResponseEntity<EyeExam> createExam(
            @PathVariable String historyId,
            @RequestBody EyeExam exam) {

        return ResponseEntity.ok(examService.createExam(historyId, exam));
    }

    // Obtener examen específico
    @GetMapping("/{historyId}/examen/{examId}")
    public ResponseEntity<EyeExam> getExam(
            @PathVariable String historyId,
            @PathVariable String examId) {

        return ResponseEntity.ok(examService.getExam(examId));
    }

    // Listar todos los exámenes de un historial
    @GetMapping("/{historyId}/examen")
    public ResponseEntity<List<EyeExam>> getExamsByHistory(
            @PathVariable String historyId) {

        return ResponseEntity.ok(examService.getExamsByHistory(historyId));
    }
}