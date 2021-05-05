import { HttpHeaders } from '@angular/common/http';
import { HttpClient } from '@angular/common/http';
import { Inject, Injectable } from '@angular/core';
import { element } from 'protractor';
import { Observable } from 'rxjs';
import { map } from 'rxjs/operators';
import { API_BASE_URL } from '../injection-tokens/api-base-url-token';
import { BotInstance } from '../models/bot-instance.model';

@Injectable({
  providedIn: 'root'
})
export class InstancesService {

  constructor(
    private http: HttpClient,
    @Inject(API_BASE_URL) private baseUrl: string
  ) { }

  getInstances(): Observable<BotInstance[]> {
    return this.http.get<BotInstance[]>(this.baseUrl + 'get_instances').pipe(
      map(res => this.mapDtoToModel(res))
    );
  }

  postInstance(instanceDto: any) {
    return this.http.post<string>(this.baseUrl + 'add_bot_instance', instanceDto);
  }

  startInstance(instanceId: any): Observable<any> {
    let headers = new HttpHeaders()
      .set('instance_id', instanceId);
    return this.http.get<any>(this.baseUrl + "/start_bot_instance", {headers});
  }

  stopInstance(instanceId: any): Observable<any> {
    let headers = new HttpHeaders()
      .set('instance_id', instanceId);
    return this.http.get<any>(this.baseUrl + "/stop_bot_instance", {headers});
  }

  deleteInstance(instanceId: any): Observable<any> {
    let headers = new HttpHeaders()
      .set('instance_id', instanceId);
    return this.http.get<any>(this.baseUrl + "/remove_bot_instance", {headers})
  }

  private mapDtoToModel(res) {
    let botInstances: BotInstance[] = [];
    res.forEach(el => {
      let botInstance: BotInstance = {
        instanceId: el["instance_id"],
        symbol: el["symbol"],
        patternId: el["pattern_id"]
      };
      botInstances.push(botInstance);
    });
    return botInstances;
  }
}
