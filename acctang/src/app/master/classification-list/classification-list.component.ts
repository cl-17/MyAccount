import { Component, Input } from '@angular/core';

import { ClassificationService } from '../../shared/services/classification.service';
import { Classification } from '../../shared/models/classification.model';

@Component({
    selector: 'classification-list',
    templateUrl: './classification-list.component.html',
    styleUrls: ['./classification-list.component.css']
})
export class ClassificationListComponent {

    title: string = '＜分類マスタ一覧＞';
    classifications: Classification[];
    selected: Classification;
    
    @Input() added: Classification = new Classification();

    constructor(
        private classificationService: ClassificationService,
    ){}
    
    ngOnInit(): void {
        this.classificationService.getAll()
            .then(res => this.classifications = res);
    }

    onSelect(classification: Classification): void {
        this.selected = classification;
    }

    onAdd(): void {
        this.classificationService.create(this.added)
            .then(res => {
                this.classifications.push(res);
                this.selected = res;
                this.added = new Classification();
            });
    }

    onDelete(classification: Classification): void {
        let index = this.classifications.indexOf(classification);
        this.classificationService.delete(classification)
            .then(() => {
                this.classifications.splice(index, 1);
                this.selected = null;
            });
    }

    onUpdate(classification: Classification): void {
        let index = this.classifications.indexOf(classification);
        this.classificationService.update(classification)
            .then(res => {
                this.classifications[index] = res;
                this.selected = res;
            });
    }

}

