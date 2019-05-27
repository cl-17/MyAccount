import { Component, Input } from '@angular/core';

import { Expense } from '../../shared/models/expense.model';

@Component({
    selector: 'expense-list',
    templateUrl: './expense-list.component.html',
    styleUrls: ['./expense-list.component.css']
})
export class ExpenseListComponent {

    selected: Expense;
    
    @Input() expenses: Expense[];
    
    constructor(
    ){}
    
    ngOnInit(): void {
    }

    onSelect(expense: Expense): void {
        this.selected = expense;
    }

    onAddEvent(expense: Expense): void {
        this.expenses.push(expense);
        this.onSelect(expense);
    }

    onUpdateEvent(expense: Expense): void {
        let index = this.expenses.indexOf(this.selected);
        this.expenses[index] = expense;
        this.onSelect(expense);
    }

    onDeleteEvent(): void {
        let index = this.expenses.indexOf(this.selected);
        this.expenses.splice(index, 1);
        this.selected = null;
    }

}

