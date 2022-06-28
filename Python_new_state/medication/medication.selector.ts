import { createFeatureSelector, createSelector } from '@ngrx/store';
import { MedicationState } from "./medication.state";

export const selectMedicationState = createFeatureSelector<MedicationState>(
    'medication'
)

export const getMedications = createSelector(
    selectMedicationState,
    state => {
        return state.medications
    }
)