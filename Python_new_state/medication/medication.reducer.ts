import { MedicationActions, MedicationActionType } from "./medication.actions";
import { MedicationState } from "./medication.state";

const initialSate: MedicationState = {
    medications: [],
    errorMessage: ""
}

export function medicationReducer(state:MedicationState = initialSate, action: MedicationActions): MedicationState{
    switch(action.type){
        case MedicationActionType.GET_MEDICATIONS:{
            return {
                ...state,
                medications: [],
                errorMessage: ""
            }
        }
        case MedicationActionType.GET_MEDICATIONS_SUCCESS:{
            return {
                ...state,
                medications: action.payload,
                errorMessage: ""
            }
        }
        case MedicationActionType.GET_MEDICATIONS_FAILED:{
            return {
                ...state,
                medications: [],
                errorMessage: action.payload["error"]
            }
        }
        default:
            return state;
    }
}