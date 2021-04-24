import { Component, OnInit } from '@angular/core';
import { DashboardService } from '../services/dashboard.service';
import { MatIconModule } from '@angular/material/icon';

@Component({
  selector: 'app-container',
  templateUrl: './container.component.html',
  styleUrls: ['./container.component.css']
})
export class ContainerComponent implements OnInit {

  constructor(private dashboardService: DashboardService) { }

  ngOnInit(): void {
    this.dashboardService.getContainerObservable().subscribe(x => {
      this.botInstanceList = false;
      this.addInstance = false;
      this.dashboard = true;
      this.addInstanceButton = false;
      this.backButton = true;
    });
  }

  botInstanceList = true;
  addInstance = false;
  dashboard = false;
  addInstanceButton = true;
  backButton = false;

  showAddInstance() {
    this.botInstanceList = false;
    this.addInstance = true;
    this.dashboard = false;
    this.addInstanceButton = false;
    this.backButton = true;
  }

  showBotInstanceList() {
    this.botInstanceList = true;
    this.addInstance = false;
    this.dashboard = false;
    this.addInstanceButton = true;
    this.backButton = false;
  }

}
