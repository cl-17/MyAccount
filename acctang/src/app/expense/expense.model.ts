import { User } from '../user/user.model';
import { Purpose } from '../purpose/purpose.model';

export class Expense {
    id: number;
    date: Date;
    classification_id: string;
    sub_id: string;
    purpose: Purpose;
    ammount: number;
    create_user_id: number;
    create_user: User;
    update_user_id: number;
    update_user: User;
    credit: boolean;

    constructor() {
        this.purpose = new Purpose;
    }
}

export class InputExpense {
    date: string;
    c_name: string;
    p_name: string;
    ammount: string;
    credit: string;
}
