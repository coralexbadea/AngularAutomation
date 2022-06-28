import { Action } from "@ngrx/store";

export enum IntoleranceActionType { 
    GET_INTOLERANCES = '[Intolerance] - Get Intolerances', 
    GET_INTOLERANCES_SUCCESS = '[Intolerance] Get intolerances success', 
    GET_INTOLERANCES_FAILED = '[Intolerance] Get intolerances failed'
}
export class GetIntolerances implements Action{ 
    readonly type = IntoleranceActionType.GET_INTOLERANCES; 
    constructor(){}; 
} 
export class GetIntolerancesSuccess implements Action{ 
    readonly type = IntoleranceActionType.GET_INTOLERANCES_SUCCESS; 
    constructor(public payload: any){}; 
} 
export class GetIntolerancesFailed implements Action{ 
    readonly type = IntoleranceActionType.GET_INTOLERANCES_FAILED; 
    constructor(public payload: any){}; 
} 
export type IntoleranceActions = GetIntolerances | GetIntolerancesSuccess | GetIntolerancesFailed;