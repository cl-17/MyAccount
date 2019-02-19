import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { MainPageComponent } from './mainpage/mainpage.component';
import { PagenotfoundComponent } from './pagenotfound/pagenotfound.component';
import { MasterMainComponent } from './master/master-main/master-main.component';
import { ClassificationListComponent } from './master/classification-list/classification-list.component';
import { PurposeListComponent } from './master/purpose-list/purpose-list.component';
import { TransactionMainComponent } from './transaction/transaction-main/transaction-main.component';
import { ExpenseListComponent } from './transaction/expense-list/expense-list.component';
import { ExpenseInputComponent } from './transaction/expense-input/expense-input.component';

const routes: Routes = [
  { path: 'angular', component: MainPageComponent },
  { path: 'angular/master', component: MasterMainComponent,
    children: [
      { path: 'classification-list', component: ClassificationListComponent },
      { path: 'purpose-list', component: PurposeListComponent },
    ]
  },
  { path: 'angular/transaction', component: TransactionMainComponent,
    children: [
      { path: 'expense-list', component: ExpenseListComponent },
      { path: 'expense-input', component: ExpenseInputComponent },
    ]
  },
  { path: '**', component: PagenotfoundComponent },
];

@NgModule({
  imports: [ RouterModule.forRoot(routes) ],
  exports: [ RouterModule ]
})
export class AppRoutingModule { }
