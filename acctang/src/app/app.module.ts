import { BrowserModule } from '@angular/platform-browser';
import { Injectable, NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { RouterModule } from '@angular/router';
import { HttpClientModule, HttpClientXsrfModule, HTTP_INTERCEPTORS, HttpInterceptor, HttpXsrfTokenExtractor, HttpRequest, HttpHandler, HttpEvent } from '@angular/common/http';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { PagenotfoundComponent } from './pagenotfound/pagenotfound.component';
import { ClassificationService } from './classification/classification.service';
import { ClassificationListComponent } from './classification/classification-list.component';
import { PurposeService } from './purpose/purpose.service';
import { PurposeListComponent } from './purpose/purpose-list.component';
import { ExpenseService } from './expense/expense.service';
import { ExpenseListComponent } from './expense/expense-list.component';
import { ExpenseInputComponent } from './expense/expense-input.component';
import { IncomeService } from './income/income.service';
import { IncomeListComponent } from './income/income-list.component';

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
    ClassificationListComponent,
    PurposeListComponent,
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

