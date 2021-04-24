import { Injectable } from '@angular/core';
import { Observable, Subscriber } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class DashboardService {

  constructor() { }

  containerSubscriber: Subscriber<any>;
  chartSubscriber: Subscriber<any>;

  public instanceId: string;

  containerObservable: Observable<any> = new Observable(subscriber => {
    this.containerSubscriber = subscriber;
  });

  chartObservable: Observable<any> = new Observable(subscriber => {
    this.chartSubscriber = subscriber;
  });

  getContainerObservable(): Observable<any> {
    return this.containerObservable;
  }

  getChartObservable(): Observable<any> {
    return this.chartObservable;
  }

  notifyContainerObserver() {
    this.containerSubscriber.next();
  }

  notifyChartObserver(data: any) {
    this.chartSubscriber.next(data);
  }

}
