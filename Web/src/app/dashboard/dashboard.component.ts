import { Component, OnInit } from '@angular/core';
import { InstanceDetails } from '../models/instance-details.model';
import { Trade } from '../models/trade.model';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent implements OnInit {

  constructor() { }

  ngOnInit(): void {
  }

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
