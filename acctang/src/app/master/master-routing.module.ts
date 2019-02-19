import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { PagenotfoundComponent } from '../pagenotfound/pagenotfound.component';
import { MasterMainComponent } from './master-main/master-main.component';
import { ClassificationListComponent } from './classification-list/classification-list.component';
import { PurposeListComponent } from './purpose-list/purpose-list.component';

const routes: Routes = [
  {path: "/", component: MasterMainComponent},
  {path: "/classification-list", component: ClassificationListComponent},
  {path: "/purpose-list", component: PurposeListComponent},
  {path: "**", component: PagenotfoundComponent },
];

@NgModule({
  imports: [ RouterModule.forRoot(routes) ],
  exports: [ RouterModule ]
})
export class MasterRoutingModule { }
