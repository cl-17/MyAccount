import { Component } from '@angular/core';

import { ExpenseService } from '../../shared/services/expense.service';
import { Expense } from '../../shared/models/expense.model';

@Component({
    selector: 'expense-register',
    templateUrl: './expense-register.component.html',
    styleUrls: ['./expense-register.component.css']
})
export class ExpenseRegisterComponent {

    title: string = '＜支出登録＞';
    enableAdd: Boolean;
    addData: Expense[];

    constructor(
        private expenseService: ExpenseService,
    ){
        this.enableAdd = true;
    }
    
    ngOnInit(): void {
    }

}

