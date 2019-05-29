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

    @Input() input_data: Expense;
    @Input() enableAdd: Boolean;

    @Output() onAddEvent = new EventEmitter<Expense>();
    @Output() onUpdateEvent = new EventEmitter<Expense>();
    @Output() onDeleteEvent = new EventEmitter<void>();

    constructor(
        private expenseService: ExpenseService,
        private classificationService: ClassificationService,
        private purposeService: PurposeService,
    ){}
    
    ngOnInit(): void {
        this.classificationService.getAll()
            .then(res => this.classifications = res);
        this.purposeService.getAllSub(this.input_data.classification_id)
            .then(res => this.purposes = res);
    }

    onClickAdd(): void {
        this.expenseService.create(this.input_data)
            .then(res => {
                this.onAddEvent.emit(res);
                this.input_data = new Expense();
            });
    }

    onClickUpdate(): void {
        this.expenseService.update(this.input_data)
            .then(res => {
                this.onUpdateEvent.emit(res);
            });
    }

    onClickDelete(): void {
        this.expenseService.delete(this.input_data)
            .then(() => {
                this.onDeleteEvent.emit();
            });
    }

    onChange(c_id: string): void {
        this.purposeService.getAllSub(c_id)
            .then(res => this.purposes = res);
        this.input_data.sub_id = null;
    }

}

