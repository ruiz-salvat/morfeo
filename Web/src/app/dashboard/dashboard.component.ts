import { Component, OnInit } from '@angular/core';
import { InstanceDetails } from '../models/instance-details.model';
import { Trade } from '../models/trade.model';
import { DashboardService } from '../services/dashboard.service';
import { InstanceDetailsService } from '../services/instance-details.service';
import { TradesService } from '../services/trades.service';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent implements OnInit {

  constructor(
    private instanceSatesDetails: InstanceDetailsService,
    private tradesService: TradesService,
    private dashboardService: DashboardService
  ) { }

  ngOnInit(): void {
    let instanceId = this.dashboardService.instanceId;
    this.instanceSatesDetails.getInstanceDetails(instanceId).subscribe(res => {
      this.instanceDetails = res;
    });
    this.tradesService.getTradesList(instanceId).subscribe(res => {
      this.trades = res;
    });
    this.tradesService.getTradesListChart(instanceId).subscribe(res => {
      this.dashboardService.notifyChartObserver(res);
    });
  }

  instanceDetails: InstanceDetails;
  trades: Trade[];
}
