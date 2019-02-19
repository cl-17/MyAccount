import { BrowserModule } from '@angular/platform-browser';
import { Injectable, NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { HttpClientModule, HttpClientXsrfModule, HTTP_INTERCEPTORS, HttpInterceptor, HttpXsrfTokenExtractor, HttpRequest, HttpHandler, HttpEvent } from '@angular/common/http';

import { MasterMainComponent } from './master-main/master-main.component';
import { ClassificationListComponent } from '../master/classification-list/classification-list.component';
import { PurposeListComponent } from '../master/purpose-list/purpose-list.component';

import { ClassificationService } from '../shared/services/classification.service';
import { PurposeService } from '../shared/services/purpose.service';

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
    MasterMainComponent,
    ClassificationListComponent,
    PurposeListComponent,
  ],
  imports: [
    BrowserModule,
    FormsModule,
    HttpClientModule,
    HttpClientXsrfModule.withOptions({
      cookieName: 'csrftoken',
      headerName: 'X-CSRFToken',
    }),
  ],
  providers: [
    ClassificationService,
    PurposeService,
    HttpXsrfInterceptor,
    { provide: HTTP_INTERCEPTORS, useExisting: HttpXsrfInterceptor, multi: true },
  ],
  bootstrap: [
  ]
})
export class MasterModule { }

