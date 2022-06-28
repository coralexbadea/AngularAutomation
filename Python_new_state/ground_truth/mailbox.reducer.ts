import { MailboxActions, MailboxActionType } from "./mailbox.actions";
import { MailboxState } from "./mailbox.state";

const initialSate: MailboxState = {
    mailboxes: [],
    errorMessage: ""
}

export function mailboxReducer(state:MailboxState = initialSate, action: MailboxActions): MailboxState{
    switch(action.type){
        case MailboxActionType.GET_MAILBOXES:{
            return {
                ...state,
                mailboxes: [],
                errorMessage: ""
            }
        }
        case MailboxActionType.GET_MAILBOXES_SUCCESS:{
            return {
                ...state,
                mailboxes: action.payload,
                errorMessage: ""
            }
        }
        case MailboxActionType.GET_MAILBOXES_FAILED:{
            return {
                ...state,
                mailboxes: [],
                errorMessage: action.payload["error"]
            }
        }
        default:
            return state;
    }
}
