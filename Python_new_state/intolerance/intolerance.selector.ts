import { createFeatureSelector, createSelector } from '@ngrx/store';
import { IntoleranceState } from "./intolerance.state";

export const selectIntoleranceState = createFeatureSelector<IntoleranceState>(
    'intolerance'
)

export const getIntolerances = createSelector(
    selectIntoleranceState,
    state => {
        return state.intolerances
    }
)