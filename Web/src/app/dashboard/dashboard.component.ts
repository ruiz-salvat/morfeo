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
    private instanceSatesService: InstanceDetailsService,
    private tradesService: TradesService,
    private dashboardService: DashboardService
  ) { }

  ngOnInit(): void {
    this.instanceSatesService.getInstanceStates().subscribe(res => {
      this.instanceDetails = res;
    });
    this.tradesService.getTradesList().subscribe(res => {
      this.trades = res;
      this.dashboardService.notifyChartObserver(res);
    });
  }

  instanceDetails: InstanceDetails;
  trades: Trade[];
}
