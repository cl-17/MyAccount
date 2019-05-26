import { Component } from '@angular/core';

import { ExpenseService } from '../../shared/services/expense.service';


@Component({
    selector: 'expense-search',
    templateUrl: './expense-search.component.html',
    styleUrls: ['./expense-search.component.css']
})
export class ExpenseSearchComponent {

    title: string = '＜＞';

    constructor(
        private expenseService: ExpenseService,
    ){
    }
    
    ngOnInit(): void {
    }

}

