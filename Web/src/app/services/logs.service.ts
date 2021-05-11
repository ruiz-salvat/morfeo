import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Inject, Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { API_BASE_URL } from '../injection-tokens/api-base-url-token';
import { map } from 'rxjs/operators';
import { Log } from '../models/log.model';
import * as moment from 'moment';

@Injectable({
  providedIn: 'root'
})
export class LogsService {

  constructor(
    private http: HttpClient,
    @Inject(API_BASE_URL) private baseUrl: string
  ) { }

  getAllLogs(): Observable<Log[]> {
    return this.http.get<Log[]>(this.baseUrl + "get_all_logs").pipe(
      map(res => this.convertToString(res))
    );
  }

  getFilteredLogs(filters: any): Observable<Log[]> {
    let headers = new HttpHeaders(filters);
    return this.http.get<Log[]>(this.baseUrl + "get_filtered_logs", {headers}).pipe(
      map(res => this.convertToString(res))
    );
  }

  private convertToString(res): Log[] {
    let logs: Log[] = [];
    for (let item of Object.keys(res))
    {
      let timestamp: number = Number(item);
      let timestampStr = moment.unix(timestamp).format("DD/MM/YYYY HH:mm")
      let log: Log = {
        date: timestampStr, 
        message: res[item]
      };
      logs.push(log);
    }
    return logs;
  }
}
