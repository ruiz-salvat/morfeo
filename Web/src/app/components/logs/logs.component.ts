import { Component, OnInit } from '@angular/core';
import { LogsService } from '../../services/logs.service';

@Component({
  selector: 'app-logs',
  templateUrl: './logs.component.html',
  styleUrls: ['./logs.component.css']
})
export class LogsComponent implements OnInit {

  constructor(private logsService: LogsService) { }

  ngOnInit(): void {
    this.logsService.getAllLogs().subscribe(res => {
      this.logText = res;
    });
  }

  logText = ["Loading..."];

}
