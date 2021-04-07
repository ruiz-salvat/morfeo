import { Injectable } from '@angular/core';
import { Observable, Subscriber } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class DashboardService {

  constructor() { }

  subscriber: Subscriber<any>;

  observable: Observable<any> = new Observable(subscriber => {
    this.subscriber = subscriber;
  });

  getObservable(): Observable<any> {
    return this.observable;
  }

  notifyObserver() {
    this.subscriber.next();
  }

}
