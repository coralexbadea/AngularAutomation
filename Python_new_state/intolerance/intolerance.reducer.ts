import { IntoleranceActions, IntoleranceActionType } from "./intolerance.actions";
import { IntoleranceState } from "./intolerance.state";

const initialSate: IntoleranceState = {
    intolerances: [],
    errorMessage: ""
}

export function intoleranceReducer(state:IntoleranceState = initialSate, action: IntoleranceActions): IntoleranceState{
    switch(action.type){
        case IntoleranceActionType.GET_INTOLERANCES:{
            return {
                ...state,
                intolerances: [],
                errorMessage: ""
            }
        }
        case IntoleranceActionType.GET_INTOLERANCES_SUCCESS:{
            return {
                ...state,
                intolerances: action.payload,
                errorMessage: ""
            }
        }
        case IntoleranceActionType.GET_INTOLERANCES_FAILED:{
            return {
                ...state,
                intolerances: [],
                errorMessage: action.payload["error"]
            }
        }
        default:
            return state;
    }
}