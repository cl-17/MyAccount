import { Injectable } from "@angular/core";
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Expense, InputExpense } from '../expense/expense.model';

'rxjs/add/operator/toPromise';

@Injectable()
export class ExpenseService {

    private url_expense: string = `http://127.0.0.1:18000/transaction_api/expense/`;
    private headers: HttpHeaders = new HttpHeaders({ 'Content-Type': 'application/json' });

    constructor(
        private http: HttpClient,
    ){
    }

    public getAll(): Promise<Expense[]> {
        const url = `${this.url_expense}get-all/`;
        return this.http.get(url, {headers: this.headers})
            .toPromise()
            .then((res) => res as Expense[])
            .catch(this.errorHandler);
    }

    public getNewPK(): Promise<number> {
        const url = `${this.url_expense}get-next-key/`;
        return this.http.get(url, {headers: this.headers})
            .toPromise()
            .then((res) => res['next_key'] as number)
            .catch(this.errorHandler);
    }

    public inputCSV(data: InputExpense[]): Promise<void> {
        const url = `${this.url_expense}input-csv/`;
        return this.http.post(url, data, {headers: this.headers})
            .toPromise()
            .then(() => null)
            .catch(this.errorHandler);
    }

    public create(added: Expense): Promise<Expense> {
        return this.getNewPK()
            .then((res) => {
                added.id = res
                return this.http.post(this.url_expense, added, {headers: this.headers})
                    .toPromise()
                    .then((res) => res as Expense)
                    .catch(this.errorHandler);
            })
            .catch(this.errorHandler);
    }

    public delete(deleted: Expense): Promise<void> {
        const url = `${this.url_expense}${deleted.id}/`;
        return this.http.delete(url, {headers: this.headers})
            .toPromise()
            .then(() => null)
            .catch(this.errorHandler);
    }

    public update(updated: Expense): Promise<Expense> {
        const url = `${this.url_expense}${updated.id}/`;
        // セッション管理するようになったら、ちゃんと取得すること
        updated.update_user_id = 2
        return this.http.put(url, updated, {headers: this.headers})
            .toPromise()
            .then((res) => res as Expense)
            .catch(this.errorHandler);
    }

    private errorHandler(err) {
        console.log('Error occured.', err);
        return Promise.reject(err.message || err);
    }

}


