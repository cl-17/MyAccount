import { Component, Input } from '@angular/core';

import { PurposeService } from '../purpose/purpose.service';
import { Purpose } from '../purpose/purpose.model';

@Component({
    selector: 'purpose-list',
    templateUrl: '../purpose/purpose-list.component.html',
    styleUrls: ['../purpose/purpose-list.component.css']
})
export class PurposeListComponent {

    title: string = '＜用途マスタ一覧＞';
    purposes: Purpose[];
    selected: Purpose;
    
    @Input() added: Purpose = new Purpose();

    constructor(
        private purposeService: PurposeService,
    ){}
    
    ngOnInit(): void {
        this.purposeService.getAll()
            .then(res => this.purposes = res);
    }

    onSelect(purpose: Purpose): void {
        this.selected = purpose;
    }

    onAdd(): void {
        this.purposeService.create(this.added)
            .then(res => {
                this.purposes.push(res);
                this.selected = res;
                this.added = new Purpose();
            });
    }

    onDelete(purpose: Purpose): void {
        let index = this.purposes.indexOf(purpose);
        this.purposeService.delete(purpose)
            .then(() => {
                this.purposes.splice(index, 1);
                this.selected = null;
            });
    }

    onUpdate(purpose: Purpose): void {
        let index = this.purposes.indexOf(purpose);
        this.purposeService.update(purpose)
            .then(res => {
                this.purposes[index] = res;
                this.selected = res;
            });
    }

}

