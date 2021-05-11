import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Inject, Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { API_BASE_URL } from '../injection-tokens/api-base-url-token';
import { map } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class LogsService {

  constructor(
    private http: HttpClient,
    @Inject(API_BASE_URL) private baseUrl: string
  ) { }

  getAllLogs(): Observable<string[]> {
    return this.http.get<string[]>(this.baseUrl + "get_all_logs").pipe(
      map(res => this.convertToString(res))
    );
  }

  getFilteredLogs(filters: any): Observable<string[]> {
    let headers = new HttpHeaders(filters);
    return this.http.get<string[]>(this.baseUrl + "get_filtered_logs", {headers}).pipe(
      map(res => this.convertToString(res))
    );
  }

  private convertToString(res): string[] {
    let messages: string[] = [];
    for (let item of Object.keys(res))
    {
      messages.push(res[item]);
    }
    return messages;
  }
}
