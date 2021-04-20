import { Component, OnInit } from '@angular/core';
import { BotInstance } from '../models/bot-instance.model';
import { DashboardService } from '../services/dashboard.service';

@Component({
  selector: 'app-instances',
  templateUrl: './instances.component.html',
  styleUrls: ['./instances.component.css']
})
export class InstancesComponent implements OnInit {

  constructor(private dashboardService: DashboardService) { }

  ngOnInit(): void {
  }

  botInstances: BotInstance[] = [
    {instanceId: "1st_instance", symbol: "ADAUSDT", patternId: "WaveTrend"},
    {instanceId: "2nd_instance", symbol: "BTCEUR", patternId: "Bolt"},
    {instanceId: "3rd_instance", symbol: "LINKUSDT", patternId: "Poisson"},
    {instanceId: "4th_instance", symbol: "ETHUSDT", patternId: "LSTNN"},
    {instanceId: "5th_instance", symbol: "BNBUSDT", patternId: "Fractals"},
    {instanceId: "6th_instance", symbol: "GUMBUSD", patternId: "Entropy"}];

  showDashboard(instanceId: any) {
    this.dashboardService.notifyObserver();
  }

}
