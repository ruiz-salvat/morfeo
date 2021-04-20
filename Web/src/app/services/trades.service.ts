import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Inject, Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { API_BASE_URL } from '../injection-tokens/api-base-url-token';
import { InstanceDetails } from '../models/instance-details.model';
import { Trade } from '../models/trade.model';
import { map } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class TradesService {

  constructor(
    private http: HttpClient,
    @Inject(API_BASE_URL) private baseUrl: string
  ) { }

  getTradesList(): Observable<Trade[]> {
    let headers = new HttpHeaders().set('instance_id', '0');
    return this.http.get<Trade[]>(this.baseUrl + 'get_trades_list', {headers}).pipe(
      map(res => this.mapDtoToModel(res))
    );
  }

  private mapDtoToModel(res): Trade[] {
    return res;
  }
}
