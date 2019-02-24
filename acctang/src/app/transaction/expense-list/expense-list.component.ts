import { Component, Input } from '@angular/core';

import { ExpenseService } from '../../shared/services/expense.service';
import { Expense } from '../../shared/models/expense.model';
import { ClassificationService } from '../../shared/services/classification.service';
import { Classification } from '../../shared/models/classification.model';
import { PurposeService } from '../../shared/services/purpose.service';
import { Purpose } from '../../shared/models/purpose.model';

@Component({
    selector: 'expense-list',
    templateUrl: './expense-list.component.html',
    styleUrls: ['./expense-list.component.css']
})
export class ExpenseListComponent {

    title: string = '＜支出一覧＞';
    classifications: Classification[];
    purposes: Purpose[];
    expenses: Expense[];
    selected: Expense;
    
    @Input() added: Expense = new Expense();

    constructor(
        private expenseService: ExpenseService,
        private classificationService: ClassificationService,
        private purposeService: PurposeService,
    ){}
    
    ngOnInit(): void {
        this.expenseService.getAll()
            .then(res => this.expenses = res);
        this.classificationService.getAll()
            .then(res => this.classifications = res);
    }

    onSelect(expense: Expense): void {
        this.selected = expense;
    }

    onAdd(): void {
        this.expenseService.create(this.added)
            .then(res => {
                this.expenses.push(res);
                this.selected = res;
                this.added = new Expense();
            });
    }

    onDelete(expense: Expense): void {
        let index = this.expenses.indexOf(expense);
        this.expenseService.delete(expense)
            .then(() => {
                this.expenses.splice(index, 1);
                this.selected = null;
            });
    }

    onUpdate(expense: Expense): void {
        let index = this.expenses.indexOf(expense);
        this.expenseService.update(expense)
            .then(res => {
                this.expenses[index] = res;
                this.selected = res;
            });
    }

    onChange(c_id: string): void {
        this.purposeService.getAllSub(c_id)
            .then(res => this.purposes = res);
    }

}

