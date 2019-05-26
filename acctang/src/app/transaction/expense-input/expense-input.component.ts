import { Component } from '@angular/core';

import { ExpenseService } from '../../shared/services/expense.service';


@Component({
    selector: 'expense-input',
    templateUrl: './expense-input.component.html',
    styleUrls: ['./expense-input.component.css']
})
export class ExpenseInputComponent {

    constructor(
        private expenseService: ExpenseService,
    ){
    }
    
    ngOnInit(): void {
    }

}

