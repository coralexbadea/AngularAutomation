import { Action } from "@ngrx/store";

export enum MedicationActionType { 
    GET_MEDICATIONS = '[Medication] - Get Medications', 
    GET_MEDICATIONS_SUCCESS = '[Medication] Get medications success', 
    GET_MEDICATIONS_FAILED = '[Medication] Get medications failed'
}
export class GetMedications implements Action{ 
    readonly type = MedicationActionType.GET_MEDICATIONS; 
    constructor(){}; 
} 
export class GetMedicationsSuccess implements Action{ 
    readonly type = MedicationActionType.GET_MEDICATIONS_SUCCESS; 
    constructor(public payload: any){}; 
} 
export class GetMedicationsFailed implements Action{ 
    readonly type = MedicationActionType.GET_MEDICATIONS_FAILED; 
    constructor(public payload: any){}; 
} 
export type MedicationActions = GetMedications | GetMedicationsSuccess | GetMedicationsFailed;