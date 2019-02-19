import { Injectable } from "@angular/core";
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Classification } from '../models/classification.model';

'rxjs/add/operator/toPromise';

@Injectable()
export class ClassificationService {

    private url_classification: string = `http://127.0.0.1:18000/master_api/classification/`;
    private headers: HttpHeaders = new HttpHeaders({ 'Content-Type': 'application/json' });

    constructor(
        private http: HttpClient,
    ){
    }

    public getAll(): Promise<Classification[]> {
        const url = `${this.url_classification}get-all/`;
        return this.http.get(url, {headers: this.headers})
            .toPromise()
            .then((res) => res as Classification[])
            .catch(this.errorHandler);
    }

    public getNewPK(): Promise<string> {
        const url = `${this.url_classification}get-next-key/`;
        return this.http.get(url, {headers: this.headers})
            .toPromise()
            .then((res) => res['next_key'] as string)
            .catch(this.errorHandler);
    }

    public create(added: Classification): Promise<Classification> {
        return this.getNewPK()
            .then((res) => {
                added.id = res
                // セッション管理するようになったら、ちゃんと取得すること
                added.update_user_id = 1
                return this.http.post(this.url_classification, added, {headers: this.headers})
                    .toPromise()
                    .then((res) => res as Classification)
                    .catch(this.errorHandler);
            })
            .catch(this.errorHandler);
    }

    public delete(deleted: Classification): Promise<void> {
        const url = `${this.url_classification}${deleted.id}/`;
        return this.http.delete(url, {headers: this.headers})
            .toPromise()
            .then(() => null)
            .catch(this.errorHandler);
    }

    public update(updated: Classification): Promise<Classification> {
        const url = `${this.url_classification}${updated.id}/`;
        // セッション管理するようになったら、ちゃんと取得すること
        updated.update_user_id = 2
        return this.http.put(url, updated, {headers: this.headers})
            .toPromise()
            .then((res) => res as Classification)
            .catch(this.errorHandler);
    }

    private errorHandler(err) {
        console.log('Error occured.', err);
        return Promise.reject(err.message || err);
    }

}


