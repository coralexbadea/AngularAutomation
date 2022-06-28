import os 

def createActions(root_folder, singular, plural):
    file_path = os.path.join(root_folder, f"{singular}.actions.ts")
    f = open(file_path, 'w')
    
    sing_cap = singular.capitalize()
    sing_upp = singular.upper()
    pl_cap = plural.capitalize()
    pl_upp = plural.upper()
    
    string = "import { Action } from \"@ngrx/store\";\n\n\
export enum "+sing_cap+"ActionType { \n\
    GET_"+pl_upp+" = '["+sing_cap+"] - Get "+pl_cap+"', \n\
    GET_"+pl_upp+"_SUCCESS = '["+sing_cap+"] Get "+plural+" success', \n\
    GET_"+pl_upp+"_FAILED = '["+sing_cap+"] Get "+plural+" failed'\n}\nexport class Get"+pl_cap+" implements Action{ \n " + \
"   readonly type = "+sing_cap+"ActionType.GET_"+pl_upp+"; \n\
    constructor(){}; \n} \n\
export class Get"+pl_cap+"Success implements Action{ \n\
    readonly type = "+sing_cap+"ActionType.GET_"+pl_upp+"_SUCCESS; \n\
    constructor(public payload: any){}; \n} \n"+"export class Get"+pl_cap+"Failed implements Action{ \n\
    readonly type = "+sing_cap+"ActionType.GET_"+pl_upp+"_FAILED; \n\
    constructor(public payload: any){}; \n} \n\
export type "+sing_cap+"Actions = Get"+pl_cap+" | Get"+pl_cap+"Success | Get"+pl_cap+"Failed;" 

    f.write(string)
    f.close()
    print("create actions stage completed")
    
def createEffects(root_folder, singular, plural):
    file_path = os.path.join(root_folder, f"{singular}.effects.ts")
    f = open(file_path, 'w')
    
    sing_cap = singular.capitalize()
    sing_upp = singular.upper()
    pl_cap = plural.capitalize()
    pl_upp = plural.upper()
    
    string = "import { Injectable } from \"@angular/core\";\n\
import { Actions, createEffect} from \'@ngrx/effects\';\n\
import { of } from \"rxjs\";\n\n"+\
"import { map, switchMap, catchError } from 'rxjs/operators';\n\
import { ofType } from \"@ngrx/effects\";\n\
import { "+sing_cap+"Service } from \"../services/"+singular+".service\";\n\
import { Get"+pl_cap+", Get"+pl_cap+"Failed, Get"+pl_cap+"Success, "+sing_cap+"ActionType } from \"./"+singular+".actions\";\n@Injectable()\n"+\
"export class Get"+pl_cap+"Effects{\n\
    constructor(\n\
        private actions: Actions,\n\
        private "+singular+"Service: "+sing_cap+"Service,\n\
    ){}\n\n\
    Get"+pl_cap+"$ = createEffect(() => this.actions.pipe(\n\
        ofType("+sing_cap+"ActionType.GET_"+pl_upp+"),\n\
        switchMap((action: Get"+pl_cap+") => {\n\
            return this."+singular+"Service.get"+pl_cap+"()\n\
            .pipe(\n\
                map(("+singular+") => {\n\
                    return new Get"+pl_cap+"Success("+singular+");\n\
                }),\n\
                catchError(error => of(new Get"+pl_cap+"Failed(error)))\n\
            )\n\
        })\n\
    ))\n\
}"
    f.write(string)
    f.close()
    print("create effects stage completed")

def createReducer(root_folder, singular, plural):
    file_path = os.path.join(root_folder, f"{singular}.reducer.ts")
    f = open(file_path, 'w')
    
    sing_cap = singular.capitalize()
    sing_upp = singular.upper()
    pl_cap = plural.capitalize()
    pl_upp = plural.upper()
    
    string = "import { "+sing_cap+"Actions, "+sing_cap+"ActionType } from \"./"+singular+".actions\";\n\
import { "+sing_cap+"State } from \"./"+singular+".state\";\n\n\
const initialSate: "+sing_cap+"State = {\n\
    "+plural+": [],\n\
    errorMessage: \"\"\n\
}\n\n\
export function "+singular+"Reducer(state:"+sing_cap+"State = initialSate, action: "+sing_cap+"Actions): "+sing_cap+"State{\n\
    switch(action.type){\n\
        case "+sing_cap+"ActionType.GET_"+pl_upp+":{\n\
            return {\n\
                ...state,\n\
                "+plural+": [],\n\
                errorMessage: \"\"\n\
            }\n\
        }\n\
        case "+sing_cap+"ActionType.GET_"+pl_upp+"_SUCCESS:{\n\
            return {\n\
                ...state,\n\
                "+plural+": action.payload,\n\
                errorMessage: \"\"\n\
            }\n\
        }\n\
        case "+sing_cap+"ActionType.GET_"+pl_upp+"_FAILED:{\n\
            return {\n\
                ...state,\n\
                "+plural+": [],\n\
                errorMessage: action.payload[\"error\"]\n\
            }\n\
        }\n\
        default:\n\
            return state;\n\
    }\n\
}"

    f.write(string)
    f.close()
    print("create reducer stage completed")
    
def createSelector(root_folder, singular, plural):
    file_path = os.path.join(root_folder, f"{singular}.selector.ts")
    f = open(file_path, 'w')
    
    sing_cap = singular.capitalize()
    sing_upp = singular.upper()
    pl_cap = plural.capitalize()
    pl_upp = plural.upper()
    
    string = "import { createFeatureSelector, createSelector } from '@ngrx/store';\n\
import { "+sing_cap+"State } from \"./"+singular+".state\";\n\n\
export const select"+sing_cap+"State = createFeatureSelector<"+sing_cap+"State>(\n\
    '"+singular+"'\n)\n\n\
export const get"+pl_cap+" = createSelector(\n\
    select"+sing_cap+"State,\n\
    state => {\n\
        return state."+plural+"\n\
    }\n\
)"
    f.write(string)
    
    print("create selector stage completed")
   
def createState(root_folder, singular, plural):
    file_path = os.path.join(root_folder, f"{singular}.state.ts")
    f = open(file_path, 'w')
    
    sing_cap = singular.capitalize()
    sing_upp = singular.upper()
    pl_cap = plural.capitalize()
    pl_upp = plural.upper()
    
    string = "export interface "+sing_cap+"State{\n\
    "+plural+": [],\n\
    errorMessage: String\n\
}"
    f.write(string)
    
    print("create state stage completed")
      
def printModule(root_folder, singular, plural):

    sing_cap = singular.capitalize()
    sing_upp = singular.upper()
    pl_cap = plural.capitalize()
    pl_upp = plural.upper()
    
    string = "     StoreModule.forFeature('"+singular+"', "+singular+"Reducer), EffectsModule.forFeature([Get"+pl_cap+"Effects]),"

    print(string)
      
    
    

if __name__ == "__main__":
    singular = input("Enter singular: ")
    plural = input("Enter plural: ")
    
    root_folder = f"./{singular}"
    if not os.path.exists(root_folder):
        os.mkdir(root_folder)
        print("Directory " , root_folder ,  " Created ")
    else:    
        print("Directory " , root_folder ,  " already exists")
    
    createActions(root_folder, singular, plural)
    createEffects(root_folder, singular, plural)
    createReducer(root_folder, singular, plural)
    createSelector(root_folder, singular, plural)
    createState(root_folder, singular, plural)
    printModule(root_folder, singular, plural)