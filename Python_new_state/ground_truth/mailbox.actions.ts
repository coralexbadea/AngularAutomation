import { Action } from "@ngrx/store";

export enum MailboxActionType {
    GET_MAILBOXES = '[Mailbox] - Get Mailboxes',
    GET_MAILBOXES_SUCCESS = '[Mailbox] Get mailboxes success',
    GET_MAILBOXES_FAILED = '[Mailbox] Get mailboxes failed'
}

export class GetMailboxes implements Action{
    readonly type = MailboxActionType.GET_MAILBOXES;
    constructor(){};
}

export class GetMailboxesSuccess implements Action{
    readonly type = MailboxActionType.GET_MAILBOXES_SUCCESS;
    constructor(public payload: any){};
}

export class GetMailboxesFailed implements Action{
    readonly type = MailboxActionType.GET_MAILBOXES_FAILED;
    constructor(public payload: any){};
}

export type MailboxActions = GetMailboxes | GetMailboxesSuccess | GetMailboxesFailed; 