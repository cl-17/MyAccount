import { User } from '../user/user.model';

export class Classification {
    id: string;
    name: string;
    create_user_id: number;
    create_user: User;
    update_user_id: number;
    update_user: User;
}
