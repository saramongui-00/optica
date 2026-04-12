package edu.uptc.swii.servicio_historial.model;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

@Getter
@Setter
@AllArgsConstructor
@NoArgsConstructor
public class Rx {
    private FinalPrescription prescriptionLE;
    private FinalPrescription prescriptionRE;
    private ParamMounting paramMounting;
    private LensType lensType;
    private PupillaryDistance pupillaryDistance;
    private String observations;
}
