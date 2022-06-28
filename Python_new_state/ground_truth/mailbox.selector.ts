import { createFeatureSelector, createSelector } from '@ngrx/store';
import { MailboxState } from "./mailbox.state";

export const selectMailboxState = createFeatureSelector<MailboxState>(
    'mailbox'
)

export const getMailboxes = createSelector(
    selectMailboxState,
    state => {
        return state.mailboxes
    }
)

