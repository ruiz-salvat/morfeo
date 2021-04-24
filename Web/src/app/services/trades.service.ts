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

  getTradesList(instanceId: string): Observable<Trade[]> {
    let headers = new HttpHeaders()
      .set('instance_id', instanceId)
      .set('order', 'descending');
    return this.http.get<Trade[]>(this.baseUrl + 'get_trades_list', {headers}).pipe(
      map(res => this.mapDtoToModel(res))
    );
  }

  getTradesListChart(instanceId: string): Observable<Trade[]> {
    let headers = new HttpHeaders()
      .set('instance_id', instanceId)
      .set('order', 'ascending');
    return this.http.get<Trade[]>(this.baseUrl + 'get_trades_list', {headers}).pipe(
      map(res => this.mapDtoToModelChart(res))
    );
  }

  private mapDtoToModel(res): Trade[] {
    let trades: Trade[] = [];
    res.forEach(el => {
      let trade: Trade = {
        time: moment.unix(el["timestamp"]).format("DD/MM/YYYY HH:mm"),
        operation: el["operation"],
        price: el["price"],
        quoteAmount: el["quote_amount"],
        gain: el["gain"]
      };
      trades.push(trade);
    });
    return trades;
  }

  private mapDtoToModelChart(res): Trade[] {
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
