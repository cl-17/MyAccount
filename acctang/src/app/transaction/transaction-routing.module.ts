import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { PagenotfoundComponent } from '../pagenotfound/pagenotfound.component';
import { TransactionMainComponent } from './transaction-main/transaction-main.component';
import { ExpenseListComponent } from './expense-list/expense-list.component';
import { ExpenseInputComponent } from './expense-input/expense-input.component';

const routes: Routes = [
  {path: "/", component: TransactionMainComponent},
  {path: "/expense-list", component: ExpenseListComponent},
  {path: "/expense-input", component: ExpenseInputComponent},
  {path: "**", component: PagenotfoundComponent },
];

@NgModule({
  imports: [ RouterModule.forRoot(routes) ],
  exports: [ RouterModule ]
})
export class TransactionRoutingModule { }
