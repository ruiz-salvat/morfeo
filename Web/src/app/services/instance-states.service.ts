import { Inject, Injectable } from '@angular/core';
import { HttpClient, HttpHeaders} from '@angular/common/http';
import { Observable } from 'rxjs';
import { InstanceStates } from '../models/instance-states.model';
import { API_BASE_URL } from '../injection-tokens/api-base-url-token';

@Injectable({
  providedIn: 'root'
})
export class InstanceStatesService {

  constructor(
    private http: HttpClient,
    @Inject(API_BASE_URL) private baseUrl: string
  ) { }

  getInstanceStates(): Observable<InstanceStates> {
    let headers = new HttpHeaders().set('instance_id', '0');
    return this.http.get<InstanceStates>(this.baseUrl + 'get_instance_states', {headers});
  }
}
