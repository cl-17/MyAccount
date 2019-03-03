import { Component } from '@angular/core';
import { DomSanitizer, SafeHtml } from '@angular/platform-browser';

import { ExpenseService } from '../../shared/services/expense.service';


@Component({
    selector: 'expense-analysis',
    templateUrl: './expense-analysis.component.html',
    styleUrls: ['./expense-analysis.component.css']
})
export class ExpenseAnalysisComponent {

    title: string = '＜支出解析＞';
    pandasResult: SafeHtml;

    constructor(
        private expenseService: ExpenseService,
        private domSanitizer: DomSanitizer,
    ){}
    
    ngOnInit(): void {
    }

    onClick(): void {
    this.expenseService.getPandasResult()
        .then(res => {
            this.pandasResult = this.domSanitizer.bypassSecurityTrustHtml(res);
        });
    }

}

