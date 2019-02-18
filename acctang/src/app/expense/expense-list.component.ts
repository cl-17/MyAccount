import { Component, Input } from '@angular/core';

import { ExpenseService } from '../expense/expense.service';
import { Expense } from '../expense/expense.model';

@Component({
    selector: 'expense-list',
    templateUrl: '../expense/expense-list.component.html',
    styleUrls: ['../expense/expense-list.component.css']
})
export class ExpenseListComponent {

    title: string = '＜支出一覧＞';
    expenses: Expense[];
    selected: Expense;
    
    @Input() added: Expense = new Expense();

    constructor(
        private expenseService: ExpenseService,
    ){}
    
    ngOnInit(): void {
        this.expenseService.getAll()
            .then(res => this.expenses = res);
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

}

