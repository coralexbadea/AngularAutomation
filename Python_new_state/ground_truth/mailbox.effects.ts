import { Injectable } from "@angular/core";
import { Actions, createEffect} from '@ngrx/effects';
import { of } from "rxjs";

import { map, switchMap, catchError } from 'rxjs/operators';
import { ofType } from "@ngrx/effects";
import { MailboxService } from "../services/mailbox.service";
import { GetMailboxes, GetMailboxesFailed, GetMailboxesSuccess, MailboxActionType } from "./mailbox.actions";
@Injectable()
export class GetMailboxesEffects{
    constructor(
        private actions: Actions,
        private mailboxService: MailboxService,
    ){}

    GetMailboxes$ = createEffect(() => this.actions.pipe(
        ofType(MailboxActionType.GET_MAILBOXES),
        switchMap((action: GetMailboxes) => {
            return this.mailboxService.getMailboxes()
            .pipe(
                map((mailboxes) => {
                    return new GetMailboxesSuccess(mailboxes);
                }),
                catchError(error => of(new GetMailboxesFailed(error)))
            )
        })
    ))
}