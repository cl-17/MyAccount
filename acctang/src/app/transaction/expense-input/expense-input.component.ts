import { Component, Input, Output, EventEmitter } from '@angular/core';

import { ExpenseService } from '../../shared/services/expense.service';
import { Expense } from '../../shared/models/expense.model';
import { ClassificationService } from '../../shared/services/classification.service';
import { Classification } from '../../shared/models/classification.model';
import { PurposeService } from '../../shared/services/purpose.service';
import { Purpose } from '../../shared/models/purpose.model';


@Component({
    selector: 'expense-input',
    templateUrl: './expense-input.component.html',
    styleUrls: ['./expense-input.component.css']
})
export class ExpenseInputComponent {

    classifications: Classification[];
    purposes: Purpose[];

    @Input() input_data: Expense = new Expense();

    @Output() addEvent = new EventEmitter<Expense>();
    @Output() updateEvent = new EventEmitter<Expense>();
    @Output() deleteEvent = new EventEmitter<Expense>();

    constructor(
        private expenseService: ExpenseService,
        private classificationService: ClassificationService,
        private purposeService: PurposeService,
    ){}
    
    ngOnInit(): void {
        this.classificationService.getAll()
            .then(res => this.classifications = res);
    }

    onClickAdd(): void {
        this.expenseService.create(this.input_data)
            .then(res => {
                this.addEvent.emit(res);
                this.input_data = new Expense();
            });
    }

    onClickDelete(expense: Expense): void {
        this.expenseService.delete(expense)
            .then(() => {
                this.deleteEvent.emit(expense);
            });
    }

    onClickUpdate(expense: Expense): void {
        this.expenseService.update(expense)
            .then(res => {
                this.updateEvent.emit(res);
            });
    }

    onChange(c_id: string): void {
        this.purposeService.getAllSub(c_id)
            .then(res => this.purposes = res);
    }

}

