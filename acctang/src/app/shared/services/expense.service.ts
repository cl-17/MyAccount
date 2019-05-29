import { Injectable } from "@angular/core";
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Expense, InputExpense } from '../models/expense.model';

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
        let result: Expense[];
        return this.http.get(url, {headers: this.headers})
            .toPromise()
            .then((res) => {
                result = res as Expense[]
                result.forEach(element => {
                    element.classification_id = element.purpose.classification.id
                    element.sub_id = element.purpose.sub_id;
                })
                return result
            })
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
        let result: Expense;
        return this.getNewPK()
            .then((res) => {
                added.id = res
                return this.http.post(this.url_expense, added, {headers: this.headers})
                    .toPromise()
                    .then((res) => {
                        result = res as Expense
                        result.classification_id = result.purpose.classification.id
                        result.sub_id = result.purpose.sub_id
                        return result
                    })
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
        let result: Expense;
        // セッション管理するようになったら、ちゃんと取得すること
        updated.update_user_id = 2
        return this.http.put(url, updated, {headers: this.headers})
            .toPromise()
            .then((res) => {
                result = res as Expense
                result.classification_id = result.purpose.classification.id
                result.sub_id = result.purpose.sub_id
                return result
            })
            .catch(this.errorHandler);
    }

    public getPandasResult(): Promise<string> {
        const url = `${this.url_expense}get-pandas-result/`;
        return this.http.get(url, {headers: this.headers})
            .toPromise()
            .then((res) => res as string)
            .catch(this.errorHandler);
    }

    private errorHandler(err) {
        console.log('Error occured.', err);
        return Promise.reject(err.message || err);
    }

}


