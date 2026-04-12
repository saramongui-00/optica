package edu.uptc.swii.servicio_historial.model;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

@Getter
@Setter
@AllArgsConstructor
@NoArgsConstructor
public class MotorStatus {
    private String coverTestSCDistantVision;
    private String coverTestCCDistantVision;
    private String ppc;
    private String closeupVision;
    private Eye dominantEye;
    private String observations;

}
