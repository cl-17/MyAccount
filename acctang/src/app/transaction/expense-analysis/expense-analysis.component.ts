import { Component, Input } from '@angular/core';

import { ExpenseService } from '../../shared/services/expense.service';

@Component({
    selector: 'expense-analysis',
    templateUrl: './expense-analysis.component.html',
    styleUrls: ['./expense-analysis.component.css']
})
export class ExpenseAnalysisComponent {

    title: string = '＜支出解析＞';

    constructor(
        private expenseService: ExpenseService,
    ){}
    
    ngOnInit(): void {
    }

    onClick(): void {
    }

}

