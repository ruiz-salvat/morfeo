import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Inject, Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { API_BASE_URL } from '../injection-tokens/api-base-url-token';
import { Trade } from '../models/trade.model';
import { map } from 'rxjs/operators';
import * as moment from 'moment';

@Injectable({
  providedIn: 'root'
})
export class TradesService {

  constructor(
    private http: HttpClient,
    @Inject(API_BASE_URL) private baseUrl: string
  ) { }

  getTradesList(): Observable<Trade[]> {
    let headers = new HttpHeaders().set('instance_id', 'seed_id');
    return this.http.get<Trade[]>(this.baseUrl + 'get_trades_list', {headers}).pipe(
      map(res => this.mapDtoToModel(res))
    );
  }

  private mapDtoToModel(res): Trade[] {
    let trades: Trade[] = [];
    res.forEach(el => {
      let trade: Trade = {
        time: moment.unix(el["timestamp"]).format("YYYY-MM-DDThh:mm:ss"),
        operation: el["operation"],
        price: el["price"],
        quoteAmount: el["quote_amount"],
        gain: el["gain"]
      };
      trades.push(trade);
    });
    return trades;
  }
}
