import { Component, Input } from '@angular/core';

import { ExpenseService } from '../../shared/services/expense.service';
import { InputExpense } from '../../shared/models/expense.model';

@Component({
    selector: 'expense-input',
    templateUrl: './expense-input.component.html',
    styleUrls: ['./expense-input.component.css']
})
export class ExpenseInputComponent {

    title: string = '＜支出取込＞';
    readText: string;

    constructor(
        private expenseService: ExpenseService,
    ){}

    ngOnInit(): void {
    }

    onChangeFile(evt) {
        let file = evt.target.files[0];
        const reader = new FileReader();
        reader.readAsText(file, 'SJIS');
        reader.addEventListener('load', () => {
            this.readText = reader.result.toString();
        });
    }

    onInputCSV() {
        let inputData:InputExpense[] = [];
        let temp = this.readText.split('\r\n');
        temp.forEach((element,index) => {
            let xxx = element.split(',', 5);
            let rowData = new InputExpense;
            rowData.date = xxx[0];
            rowData.c_name = xxx[1];
            rowData.p_name = xxx[2];
            rowData.ammount = xxx[3];
            rowData.credit = xxx[4];
            if (rowData.date != '') {
                inputData[index] = rowData
            }
        });
        this.expenseService.inputCSV(inputData);
        this.readText = '';
    }

}

