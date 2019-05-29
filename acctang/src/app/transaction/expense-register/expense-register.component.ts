import { Component, Input } from '@angular/core';

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

    @Input() addData: Expense[];

    constructor(
        private expenseService: ExpenseService,
    ){
        this.addData = [];
        this.enableAdd = true;
    }
    
    ngOnInit(): void {
    }

    onAddEvent(expense: Expense): void {
        this.addData.push(expense);
    }

}

