import { Component, OnInit } from '@angular/core';
import { InstanceDetails } from '../models/instance-details.model';
import { Trade } from '../models/trade.model';
import { InstanceDetailsService } from '../services/instance-details.service';
import { TradesService } from '../services/trades.service';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent implements OnInit {

  constructor(
    private instanceSatesService: InstanceDetailsService,
    private tradesService: TradesService
  ) { }

  ngOnInit(): void {
    this.instanceSatesService.getInstanceStates().subscribe(res => {
      this.instanceDetails = res;
    });
    this.tradesService.getTradesList().subscribe(res => {
      this.trades = res;
      this.setChartData(res);
      console.log(this.data);
    });
  }

  instanceDetails: InstanceDetails;
  trades: Trade[];
  data = [{
    "value": 20,
    "date": "2020-05-12T12:19:00+00:00"
  },
  {
    "value": 30,
    "date": "2020-05-12T12:25:00+00:00"
  }];

  private setChartData(trades: Trade[]) {
    trades.forEach(t => {
      if (t.operation == "SELL") {
        /*let tradeData = {
          "value": t.gain,
          "date": t.time
        }*/
        let tradeData = {
          "value": 20,
          "date": "2020-05-12T12:19:00+00:00"
        }
        this.data.push(tradeData);
      }
    });
  }
}
