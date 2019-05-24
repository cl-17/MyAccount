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
    expressImg: boolean;

    constructor(
        private expenseService: ExpenseService,
        private domSanitizer: DomSanitizer,
    ){
        this.expressImg = false;
    }
    
    ngOnInit(): void {
    }

    onClick(): void {
        this.expenseService.getPandasResult()
            .then(res => {
                this.pandasResult = this.domSanitizer.bypassSecurityTrustHtml(res);
                this.expressImg = true;
            });
    }

    onImgError(image): void {
        image.style.display = 'none';
    }

}

