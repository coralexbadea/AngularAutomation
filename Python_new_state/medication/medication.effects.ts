import { Injectable } from "@angular/core";
import { Actions, createEffect} from '@ngrx/effects';
import { of } from "rxjs";

import { map, switchMap, catchError } from 'rxjs/operators';
import { ofType } from "@ngrx/effects";
import { MedicationService } from "../services/medication.service";
import { GetMedications, GetMedicationsFailed, GetMedicationsSuccess, MedicationActionType } from "./medication.actions";
@Injectable()
export class GetMedicationsEffects{
    constructor(
        private actions: Actions,
        private medicationService: MedicationService,
    ){}

    GetMedications$ = createEffect(() => this.actions.pipe(
        ofType(MedicationActionType.GET_MEDICATIONS),
        switchMap((action: GetMedications) => {
            return this.medicationService.getMedications()
            .pipe(
                map((medication) => {
                    return new GetMedicationsSuccess(medication);
                }),
                catchError(error => of(new GetMedicationsFailed(error)))
            )
        })
    ))
}