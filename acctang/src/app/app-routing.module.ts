import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { PagenotfoundComponent } from './pagenotfound/pagenotfound.component';
import { ClassificationListComponent } from './classification/classification-list.component';
import { PurposeListComponent } from './purpose/purpose-list.component';
import { ExpenseListComponent } from './expense/expense-list.component';
import { ExpenseInputComponent } from './expense/expense-input.component';

const routes: Routes = [
  {path: "classification-list", component: ClassificationListComponent},
  {path: "purpose-list", component: PurposeListComponent},
  {path: "expense-list", component: ExpenseListComponent},
  {path: "expense-input", component: ExpenseInputComponent},
  {path: "**", component: PagenotfoundComponent },
];

@NgModule({
  imports: [ RouterModule.forRoot(routes) ],
  exports: [ RouterModule ]
})
export class AppRoutingModule { }
