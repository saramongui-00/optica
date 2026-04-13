package edu.uptc.swii.servicio_historial.controller;

import edu.uptc.swii.servicio_historial.dto.MedicalHistoryFullDTO;
import edu.uptc.swii.servicio_historial.model.MedicalHistory;
import edu.uptc.swii.servicio_historial.service.MedicalHistoryService;
import lombok.RequiredArgsConstructor;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/historial")
@RequiredArgsConstructor
public class MedicalHistoryController {

    private final MedicalHistoryService historyService;

    @PostMapping("/patient/{patientId}")
    public ResponseEntity<MedicalHistory> createHistory(@PathVariable String patientId) {
        return ResponseEntity.ok(historyService.createMedicalHistory(patientId));
    }

    @GetMapping("/{id}")
    public ResponseEntity<MedicalHistory> getHistoryById(@PathVariable String id) {
        return ResponseEntity.ok(historyService.getById(id));
    }

    @GetMapping("/patient/{patientId}")
    public ResponseEntity<MedicalHistoryFullDTO> getFullHistory(@PathVariable String patientId) {
        return ResponseEntity.ok(historyService.getFullHistory(patientId));
    }

    //PENDIENTE
    @GetMapping("/{id}/documento")
    public String generarDocumento(@PathVariable String id){
        return "Documento HC generado correctamente";
    }

    //PENDIENTE
    @GetMapping("/{id}/rx")
    public String generarRX(@PathVariable String id){
        return "Receta final generada correctamente";
    }
}