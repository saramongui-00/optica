package edu.uptc.swii.servicio_historial.model;

public class EyeExam {
    private String appointmentReason;
    private CorrectedVisualAcuity avccLE;
    private CorrectedVisualAcuity avccRE;
    private MotorStatus motorStatus;
    private ExternalEyeExam externalEyeExamLE;
    private ExternalEyeExam externalEyeExamRE;
    private Ophthalmoscopy ophthalmoscopyLE;
    private Ophthalmoscopy ophthalmoscopyRE;
    private Keratometry keratometryLE;
    private Keratometry keratometryRE;
    private Refraction refractionLE;
    private Refraction refractionRE;
    private Diagnosis diagnosis;
    private Rx finalRX;
    private Rx previousRX;
    private String behavior;
    private String observations;
}
