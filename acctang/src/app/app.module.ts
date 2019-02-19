import { BrowserModule } from '@angular/platform-browser';
import { Injectable, NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { HttpClientModule, HttpClientXsrfModule, HTTP_INTERCEPTORS, HttpInterceptor, HttpXsrfTokenExtractor, HttpRequest, HttpHandler, HttpEvent } from '@angular/common/http';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { PagenotfoundComponent } from './pagenotfound/pagenotfound.component';
import { MasterMainComponent } from './master/master-main/master-main.component';
import { ClassificationListComponent } from './master/classification-list/classification-list.component';
import { PurposeListComponent } from './master/purpose-list/purpose-list.component';
import { TransactionMainComponent } from './transaction/transaction-main/transaction-main.component';
import { ExpenseListComponent } from './transaction/expense-list/expense-list.component';
import { ExpenseInputComponent } from './transaction/expense-input/expense-input.component';
import { IncomeListComponent } from './transaction/income-list/income-list.component';

import { ClassificationService } from './shared/services/classification.service';
import { PurposeService } from './shared/services/purpose.service';
import { ExpenseService } from './shared/services/expense.service';
import { IncomeService } from './shared/services/income.service';

import { Observable } from 'rxjs';


@Injectable()
export class HttpXsrfInterceptor implements HttpInterceptor {

  constructor(private tokenExtractor: HttpXsrfTokenExtractor) {
  }

  intercept(req: HttpRequest<any>, next: HttpHandler): Observable<HttpEvent<any>> {
    const headerName = 'X-CSRFToken';
    const token = this.tokenExtractor.getToken() as string;
    if (token !== null && !req.headers.has(headerName)) {
      req = req.clone({ headers: req.headers.set(headerName, token) });
    }
    return next.handle(req);
  }

}

@NgModule({
  declarations: [
    AppComponent,
    PagenotfoundComponent,
    MasterMainComponent,
    ClassificationListComponent,
    PurposeListComponent,
    TransactionMainComponent,
    ExpenseListComponent,
    ExpenseInputComponent,
    IncomeListComponent,
  ],
  imports: [
    BrowserModule,
    FormsModule,
    HttpClientModule,
    AppRoutingModule,
    HttpClientXsrfModule.withOptions({
      cookieName: 'csrftoken',
      headerName: 'X-CSRFToken',
    }),
  ],
  providers: [
    ClassificationService,
    PurposeService,
    ExpenseService,
    IncomeService,
    HttpXsrfInterceptor,
    { provide: HTTP_INTERCEPTORS, useExisting: HttpXsrfInterceptor, multi: true },
  ],
  bootstrap: [
    AppComponent,
  ]
})
export class AppModule { }

