package edu.uptc.swii.servicio_historial.repository;

import edu.uptc.swii.servicio_historial.model.MedicalHistory;
import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.stereotype.Repository;

import java.util.Optional;

@Repository
public interface MedicalHistoryRepository
        extends MongoRepository<MedicalHistory, String> {

    Optional<MedicalHistory> findByPatientId(String patientId);
}