import { Injectable } from "@angular/core";
import { Actions, createEffect} from '@ngrx/effects';
import { of } from "rxjs";

import { map, switchMap, catchError } from 'rxjs/operators';
import { ofType } from "@ngrx/effects";
import { IntoleranceService } from "../services/intolerance.service";
import { GetIntolerances, GetIntolerancesFailed, GetIntolerancesSuccess, IntoleranceActionType } from "./intolerance.actions";
@Injectable()
export class GetIntolerancesEffects{
    constructor(
        private actions: Actions,
        private intoleranceService: IntoleranceService,
    ){}

    GetIntolerances$ = createEffect(() => this.actions.pipe(
        ofType(IntoleranceActionType.GET_INTOLERANCES),
        switchMap((action: GetIntolerances) => {
            return this.intoleranceService.getIntolerances()
            .pipe(
                map((intolerance) => {
                    return new GetIntolerancesSuccess(intolerance);
                }),
                catchError(error => of(new GetIntolerancesFailed(error)))
            )
        })
    ))
}