import { Injectable } from '@angular/core';
import { Observable, Subscriber } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class DashboardService {

  constructor() { }

  dashboardSubscriber: Subscriber<any>;
  chartSubscriber: Subscriber<any>;

  dashboardObservable: Observable<any> = new Observable(subscriber => {
    this.dashboardSubscriber = subscriber;
  });

  chartObservable: Observable<any> = new Observable(subscriber => {
    this.chartSubscriber = subscriber;
  });

  getDashboardObservable(): Observable<any> {
    return this.dashboardObservable;
  }

  getChartObservable(): Observable<any> {
    return this.chartObservable;
  }

  notifyDashboardObserver() {
    this.dashboardSubscriber.next();
  }

  notifyChartObserver(data: any) {
    this.chartSubscriber.next(data);
  }

}
