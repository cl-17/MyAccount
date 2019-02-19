import { User } from './user.model';
import { Classification } from './classification.model';

export class Income {
    classification_id: string;
    classification: Classification;
    sub_id: string;
    name: string;
    create_user_id: number;
    create_user: User;
    update_user_id: number;
    update_user: User;

    constructor() {
        this.classification = new Classification;
    }
}
