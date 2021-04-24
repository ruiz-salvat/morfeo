import { Component, OnInit } from '@angular/core';
import { BotInstance } from '../models/bot-instance.model';
import { DashboardService } from '../services/dashboard.service';
import { InstancesService } from '../services/instances.service';

@Component({
  selector: 'app-instances',
  templateUrl: './instances.component.html',
  styleUrls: ['./instances.component.css']
})
export class InstancesComponent implements OnInit {

  constructor(
    private dashboardService: DashboardService,
    private instancesService: InstancesService) { }

  ngOnInit(): void {
    this.instancesService.getInstances().subscribe(res => {
      this.botInstances = res;
    });
  }

  botInstances: BotInstance[];

  showDashboard(instanceId: any) {
    this.dashboardService.instanceId = instanceId;
    this.dashboardService.notifyContainerObserver();
  }

}
