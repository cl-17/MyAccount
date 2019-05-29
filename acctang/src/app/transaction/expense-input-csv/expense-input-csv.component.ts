import { Component, Input } from '@angular/core';

import { ExpenseService } from '../../shared/services/expense.service';
import { InputExpense } from '../../shared/models/expense.model';

@Component({
    selector: 'expense-input-csv',
    templateUrl: './expense-input-csv.component.html',
    styleUrls: ['./expense-input-csv.component.css']
})
export class ExpenseInputCsvComponent {

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
        let csvData:InputExpense[] = [];
        let temp = this.readText.split('\r\n');
        temp.forEach((element,index) => {
            let inputData = element.split(',', 5);
            let rowData = new InputExpense;
            rowData.date = inputData[0];
            rowData.c_name = inputData[1];
            rowData.p_name = inputData[2];
            rowData.ammount = inputData[3];
            rowData.credit = inputData[4];
            if (rowData.date != '') {
                csvData[index] = rowData
            }
        });
        this.expenseService.inputCSV(csvData);
        this.readText = '';
    }

}

