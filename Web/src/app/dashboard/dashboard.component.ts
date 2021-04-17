import { Component, OnInit, ChangeDetectionStrategy } from '@angular/core';
import { InstanceDetails } from '../models/instance-details.model';
import { Trade } from '../models/trade.model';
import { InstanceStatesService } from '../services/instance-states.service';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent implements OnInit {

  constructor(
    private instanceSatesService: InstanceStatesService
  ) { }

  ngOnInit(): void {
    this.instanceSatesService.getInstanceStates().subscribe(res => {
      console.log(res);
    });
  }

  public data = [
    {
      "value": 20,
      "date": "2020-05-12T12:19:00+00:00"
    },
    {
      "value": 50,
      "date": "2020-05-14T12:19:00+00:00"
    },
    {
      "value": 30,
      "date": "2020-05-16T12:19:00+00:00"
    },
    {
      "value": 80,
      "date": "2020-05-18T12:19:00+00:00"
    },
    {
      "value": 55,
      "date": "2020-05-20T12:19:00+00:00"
    },
    {
      "value": 60,
      "date": "2020-05-22T12:19:00+00:00"
    },
    {
      "value": 45,
      "date": "2020-05-24T12:19:00+00:00"
    },
    {
      "value": 30,
      "date": "2020-05-26T12:19:00+00:00"
    },
    {
      "value": 40,
      "date": "2020-05-28T12:19:00+00:00"
    },
    {
      "value": 70,
      "date": "2020-05-30T12:19:00+00:00"
    },
    {
      "value": 63,
      "date": "2020-06-01T12:19:00+00:00"
    },
    {
      "value": 40,
      "date": "2020-06-03T12:19:00+00:00"
    },
    {
      "value": 50,
      "date": "2020-06-05T12:19:00+00:00"
    },
    {
      "value": 75,
      "date": "2020-06-07T12:19:00+00:00"
    },
    {
      "value": 20,
      "date": "2020-06-09T12:19:00+00:00"
    },
    {
      "value": 50,
      "date": "2020-06-11T12:19:00+00:00"
    },
    {
      "value": 80,
      "date": "2020-06-13T12:19:00+00:00"
    },
    {
      "value": 75,
      "date": "2020-06-15T12:19:00+00:00"
    },
    {
      "value": 82,
      "date": "2020-06-17T12:19:00+00:00"
    },
    {
      "value": 55,
      "date": "2020-06-19T12:19:00+00:00"
    },
    {
      "value": 35,
      "date": "2020-06-21T12:19:00+00:00"
    },
    {
      "value": 34,
      "date": "2020-06-23T12:19:00+00:00"
    },
    {
      "value": 45,
      "date": "2020-06-25T12:19:00+00:00"
    },
    {
      "value": 58,
      "date": "2020-06-27T12:19:00+00:00"
    },
    {
      "value": 34,
      "date": "2020-06-29T12:19:00+00:00"
    },
    {
      "value": 60,
      "date": "2020-07-01T12:19:00+00:00"
    },
    {
      "value": 75,
      "date": "2020-07-03T12:19:00+00:00"
    },
    {
      "value": 80,
      "date": "2020-07-05T12:19:00+00:00"
    },
    {
      "value": 29,
      "date": "2020-07-07T12:19:00+00:00"
    },
    {
      "value": 40,
      "date": "2020-07-09T12:19:00+00:00"
    },
    {
      "value": 54,
      "date": "2020-07-11T12:19:00+00:00"
    },
    {
      "value": 67,
      "date": "2020-07-13T12:19:00+00:00"
    },
    {
      "value": 90,
      "date": "2020-07-15T12:19:00+00:00"
    },
    {
      "value": 84,
      "date": "2020-07-17T12:19:00+00:00"
    },
    {
      "value": 43,
      "date": "2020-07-19T12:19:00+00:00"
    }
  ];

  instanceDetails: InstanceDetails = {
    instanceId: "1st_instance",
    symbol: "ADAUSDT",
    creationTime: "06-11-2017 06:15:00",
    patternId: "WaveTrend",
    timeScale: 5,
    budget: 1100,
    initialBudget: 1000,
    cleanGains: 100,
    partitionSize: 10,
    baseAmount: 14,
    nPartitions: 5,
    partitionLimit: 25
  };

  trades: Trade[] = [{
    time: "06-11-2017 06:15:00",
    operation: "BUY",
    price: 17.300,
    quoteAmount: 10,
    gain: null
  },
  {
    time: "06-11-2017 08:15:00",
    operation: "SELL",
    price: 17.55,
    quoteAmount: 12.1,
    gain: 2.1
  },
  {
    time: "06-11-2017 08:15:00",
    operation: "SELL",
    price: 17.55,
    quoteAmount: 12.1,
    gain: 2.1
  },
  {
    time: "06-11-2017 08:15:00",
    operation: "SELL",
    price: 17.55,
    quoteAmount: 12.1,
    gain: 2.1
  },
  {
    time: "06-11-2017 08:15:00",
    operation: "SELL",
    price: 17.55,
    quoteAmount: 12.1,
    gain: 2.1
  },
  {
    time: "06-11-2017 08:15:00",
    operation: "SELL",
    price: 17.55,
    quoteAmount: 12.1,
    gain: 2.1
  },
  {
    time: "06-11-2017 08:15:00",
    operation: "SELL",
    price: 17.55,
    quoteAmount: 12.1,
    gain: 2.1
  },
  {
    time: "06-11-2017 08:15:00",
    operation: "SELL",
    price: 17.55,
    quoteAmount: 12.1,
    gain: 2.1
  },
  {
    time: "06-11-2017 08:15:00",
    operation: "SELL",
    price: 17.55,
    quoteAmount: 12.1,
    gain: 2.1
  },
  {
    time: "06-11-2017 08:15:00",
    operation: "SELL",
    price: 17.55,
    quoteAmount: 12.1,
    gain: 2.1
  },
  {
    time: "06-11-2017 08:15:00",
    operation: "SELL",
    price: 17.55,
    quoteAmount: 12.1,
    gain: 2.1
  }];
}
