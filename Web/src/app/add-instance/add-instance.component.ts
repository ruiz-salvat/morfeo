import { Component, OnInit } from '@angular/core';
import { FormControl, FormGroup } from '@angular/forms';
import { InstancesService } from '../services/instances.service';

@Component({
  selector: 'app-add-instance',
  templateUrl: './add-instance.component.html',
  styleUrls: ['./add-instance.component.css']
})
export class AddInstanceComponent implements OnInit {

  constructor(
    private instancesService: InstancesService
  ) { }

  ngOnInit(): void {
  }

  addInstanceForm = new FormGroup({
    instanceId: new FormControl(''),
    symbol: new FormControl(''),
    patternId: new FormControl(''),
    timeScale: new FormControl(''),
    budget: new FormControl(''),
    partitionSize: new FormControl(''),
    partitionLimit: new FormControl(''),
    timeRangeInDays: new FormControl('')
  });

  onSubmit() {
    let instanceDto = {
      "instance_id": this.addInstanceForm.controls["instanceId"].value,
      "symbol": this.addInstanceForm.controls["symbol"].value,
      "pattern_id": this.addInstanceForm.controls["patternId"].value,
      "customer_id": "Front-End Test Customer", // TODO: store customer id in session
      "time_scale": this.addInstanceForm.controls["timeScale"].value,
      "budget": this.addInstanceForm.controls["budget"].value,
      "partition_size": this.addInstanceForm.controls["partitionSize"].value,
      "n_partition_limit": this.addInstanceForm.controls["partitionLimit"].value,
      "time_range_in_days": this.addInstanceForm.controls["timeRangeInDays"].value
    }
    this.instancesService.postInstance(instanceDto).subscribe(res => {
      document.getElementById("response").innerHTML = res;
    });
  }
}
