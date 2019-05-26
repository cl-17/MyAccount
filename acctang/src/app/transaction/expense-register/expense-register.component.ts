import { Component } from '@angular/core';

import { ExpenseService } from '../../shared/services/expense.service';


@Component({
    selector: 'expense-register',
    templateUrl: './expense-register.component.html',
    styleUrls: ['./expense-register.component.css']
})
export class ExpenseRegisterComponent {

    title: string = '＜支出登録＞';

    constructor(
        private expenseService: ExpenseService,
    ){
    }
    
    ngOnInit(): void {
    }

}

