import { Injectable } from "@angular/core";
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Purpose } from '../purpose/purpose.model';

'rxjs/add/operator/toPromise';

@Injectable()
export class PurposeService {

    private url_purpose: string = `http://127.0.0.1:18000/master_api/purpose/`;
    private headers: HttpHeaders = new HttpHeaders({ 'Content-Type': 'application/json' });

    constructor(
        private http: HttpClient,
    ){
    }

    public getAll(): Promise<Purpose[]> {
        const url = `${this.url_purpose}get-all/`;
        return this.http.get(url, {headers: this.headers})
            .toPromise()
            .then((res) => res as Purpose[])
            .catch(this.errorHandler);
    }

    public getNewPK(c_id: string): Promise<string> {
        const url = `${this.url_purpose}get-next-key/${c_id}/`;
        return this.http.get(url, {headers: this.headers})
            .toPromise()
            .then((res) => res['next_key'] as string)
            .catch(this.errorHandler);
    }

    public create(added: Purpose): Promise<Purpose> {
        return this.getNewPK(added.classification_id)
            .then((res) => {
                added.sub_id = res
                // セッション管理するようになったら、ちゃんと取得すること
                added.update_user_id = 1
                return this.http.post(this.url_purpose, added, {headers: this.headers})
                    .toPromise()
                    .then((res) => res as Purpose)
                    .catch(this.errorHandler);
            })
            .catch(this.errorHandler);
    }

    public delete(deleted: Purpose): Promise<void> {
        const url = `${this.url_purpose}${deleted.classification.id}${deleted.sub_id}/`;
        return this.http.delete(url, {headers: this.headers})
            .toPromise()
            .then(() => null)
            .catch(this.errorHandler);
    }

    public update(updated: Purpose): Promise<Purpose> {
        const url = `${this.url_purpose}${updated.classification.id}${updated.sub_id}/`;
        // セッション管理するようになったら、ちゃんと取得すること
        updated.update_user_id = 2
        return this.http.put(url, updated, {headers: this.headers})
            .toPromise()
            .then((res) => res as Purpose)
            .catch(this.errorHandler);
    }

    private errorHandler(err) {
        console.log('Error occured.', err);
        return Promise.reject(err.message || err);
    }

}


