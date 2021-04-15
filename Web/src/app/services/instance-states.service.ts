import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';
import { InstanceStates } from '../models/instance-states.model';

@Injectable({
  providedIn: 'root'
})
export class InstanceStatesService {

  constructor(
    private http: HttpClient
  ) { }

  getInstanceStates(): Observable<InstanceStates> {
    return this.http.get<InstanceStates>('');
  }
}
