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
