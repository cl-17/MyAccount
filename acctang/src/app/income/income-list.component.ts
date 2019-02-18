import { Component, Input } from '@angular/core';

import { IncomeService } from '../income/income.service';
import { Income } from '../income/income.model';
import { Classification } from '../classification/classification.model';

@Component({
    selector: 'income-list',
    templateUrl: '../income/income-list.component.html',
    styleUrls: ['../income/income-list.component.css']
})
export class IncomeListComponent {

    title: string = '＜用途マスタ一覧＞';
    incomes: Income[];
    selected: Income;
    
    @Input() added: Income = new Income();

    constructor(
        private incomeService: IncomeService,
    ){}
    
    ngOnInit(): void {
        this.incomeService.getAll()
            .then(res => this.incomes = res);
    }

    onSelect(income: Income): void {
        this.selected = income;
    }

    onAdd(): void {
        this.incomeService.create(this.added)
            .then(res => {
                this.incomes.push(res);
                this.selected = res;
                this.added = new Income();
            });
    }

    onDelete(income: Income): void {
        let index = this.incomes.indexOf(income);
        this.incomeService.delete(income)
            .then(() => {
                this.incomes.splice(index, 1);
                this.selected = null;
            });
    }

    onUpdate(income: Income): void {
        let index = this.incomes.indexOf(income);
        this.incomeService.update(income)
            .then(res => {
                this.incomes[index] = res;
                this.selected = res;
            });
    }

}

