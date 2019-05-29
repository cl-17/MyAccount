import { Component } from '@angular/core';

import { ExpenseService } from '../../shared/services/expense.service';
import { Expense } from '../../shared/models/expense.model';

@Component({
    selector: 'expense-search',
    templateUrl: './expense-search.component.html',
    styleUrls: ['./expense-search.component.css']
})
export class ExpenseSearchComponent {

    title: string = '＜支出検索＞';
    searchResult: Expense[];

    constructor(
        private expenseService: ExpenseService,
    ){
    }
    
    ngOnInit(): void {
    }

    onClickSearch(): void {
        this.expenseService.getAll()
            .then((res) => this.searchResult = res as Expense[])
    }

}

