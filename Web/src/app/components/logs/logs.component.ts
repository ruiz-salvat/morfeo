import { Component, OnInit } from '@angular/core';
import { FormControl, FormGroup } from '@angular/forms';
import { Log } from 'src/app/models/log.model';
import { LogsService } from '../../services/logs.service';

@Component({
  selector: 'app-logs',
  templateUrl: './logs.component.html',
  styleUrls: ['./logs.component.css']
})
export class LogsComponent implements OnInit {

  constructor(private logsService: LogsService) { }

  ngOnInit(): void {
    
  }

  logOptionsForm = new FormGroup({
    serviceName: new FormControl(),
    instanceId: new FormControl(),
    process: new FormControl(),
    isThread: new FormControl()
  });

  logs: Log[] = [
    {date: "",
    message: "> Select one option to retrieve logs"}
  ];

  getAllLogs() {
    this.logs = [
      {date: "",
      message: "Loading..."}
    ];
    
    this.logsService.getAllLogs().subscribe(res => {
      this.logs = res;
    });
  }

  getLogs(logType: any) {
    this.logs = [
      {date: "",
      message: "Loading..."}
    ];

    // "" is used to avoid having null parameters
    let logFiltersDto = {
      "log_type": logType,
      "service_name": "" + this.logOptionsForm.controls["serviceName"].value,
      "instance_id": "" + this.logOptionsForm.controls["instanceId"].value,
      "process": "" + this.logOptionsForm.controls["process"].value,
      "is_thread": "" + this.logOptionsForm.controls["isThread"].value,
    }
    
    this.logsService.getFilteredLogs(logFiltersDto).subscribe(res => {
      this.logs = res;
    });
  }
}
