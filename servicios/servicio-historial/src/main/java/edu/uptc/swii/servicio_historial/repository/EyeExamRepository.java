package edu.uptc.swii.servicio_historial.repository;

import edu.uptc.swii.servicio_historial.model.EyeExam;
import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface EyeExamRepository extends MongoRepository<EyeExam, String> {

    List<EyeExam> findByMedicalHistoryId(String medicalHistoryId);

}