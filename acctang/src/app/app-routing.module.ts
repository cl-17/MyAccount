import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { MainPageComponent } from './mainpage/mainpage.component';
import { PagenotfoundComponent } from './pagenotfound/pagenotfound.component';
import { MasterMainComponent } from './master/master-main/master-main.component';
import { ClassificationListComponent } from './master/classification-list/classification-list.component';
import { PurposeListComponent } from './master/purpose-list/purpose-list.component';
import { TransactionMainComponent } from './transaction/transaction-main/transaction-main.component';
import { ExpenseSearchComponent } from './transaction/expense-search/expense-search.component';
import { ExpenseInputCsvComponent } from './transaction/expense-input-csv/expense-input-csv.component';
import { ExpenseAnalysisComponent } from './transaction/expense-analysis/expense-analysis.component';

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
      { path: 'expense-search', component: ExpenseSearchComponent },
      { path: 'expense-input-csv', component: ExpenseInputCsvComponent },
      { path: 'expense-analysis', component: ExpenseAnalysisComponent },
    ]
  },
  { path: '**', component: PagenotfoundComponent },
];

@NgModule({
  imports: [ RouterModule.forRoot(routes) ],
  exports: [ RouterModule ]
})
export class AppRoutingModule { }
