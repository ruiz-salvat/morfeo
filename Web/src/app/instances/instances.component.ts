import { Component, OnInit } from '@angular/core';
import { BotInstance } from '../models/bot-instance.model';

@Component({
  selector: 'app-instances',
  templateUrl: './instances.component.html',
  styleUrls: ['./instances.component.css']
})
export class InstancesComponent implements OnInit {

  constructor() { }

  ngOnInit(): void {
  }

  botInstances: BotInstance[] = [
    {instanceId: "first_instance", symbol: "ADAUSDT", patternId: "WaveTrend"},
    {instanceId: "second_instance", symbol: "DOGEPANDA", patternId: "Bolt"}];

}
