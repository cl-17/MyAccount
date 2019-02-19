import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { PagenotfoundComponent } from './pagenotfound/pagenotfound.component';

const routes: Routes = [
  { path: 'angular/master', loadChildren: './master/master.module#MasterModule' },
  { path: 'angular/transaction', loadChildren: './transaction/transaction.module#TransactionModule' },
  { path: "**", component: PagenotfoundComponent },
];

@NgModule({
  imports: [ RouterModule.forRoot(routes) ],
  exports: [ RouterModule ]
})
export class AppRoutingModule { }
