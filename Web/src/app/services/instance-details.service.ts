import { Inject, Injectable } from '@angular/core';
import { HttpClient, HttpHeaders} from '@angular/common/http';
import { Observable } from 'rxjs';
import { API_BASE_URL } from '../injection-tokens/api-base-url-token';
import { InstanceDetails } from '../models/instance-details.model';
import { map } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class InstanceDetailsService {

  constructor(
    private http: HttpClient,
    @Inject(API_BASE_URL) private baseUrl: string
  ) { }

  getInstanceStates(): Observable<InstanceDetails> {
    let headers = new HttpHeaders().set('instance_id', '0');
    return this.http.get<InstanceDetails>(this.baseUrl + 'get_instance_details', {headers}).pipe(
      map(res => this.mapDtoToModel(res))
    );
  }

  private mapDtoToModel(res): InstanceDetails {
    let instanceDetails: InstanceDetails = {
      instanceId: res["instance_id"],
      symbol: res["symbol"],
      creationTime: res["creation_time"],
      patternId: res["pattern_id"],
      timeScale: res["time_scale"],
      budget: res["budget"],
      initialBudget: res["initial_budget"],
      cleanGains: res["clean_gains"],
      partitionSize: res["partition_size"],
      baseAmount: res["base_amount"],
      nPartitions: res["n_partitions"],
      partitionLimit: res["n_partition_limit"]
    };
    return instanceDetails;
  }
}
