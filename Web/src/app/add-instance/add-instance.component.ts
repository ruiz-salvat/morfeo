import { Component, OnInit } from '@angular/core';
import { FormControl, FormGroup } from '@angular/forms';

@Component({
  selector: 'app-add-instance',
  templateUrl: './add-instance.component.html',
  styleUrls: ['./add-instance.component.css']
})
export class AddInstanceComponent implements OnInit {

  constructor() { }

  ngOnInit(): void {
  }

  addInstanceForm = new FormGroup({
    instanceId: new FormControl(''),
    symbol: new FormControl(''),
    patternId: new FormControl(''),
    timeScale: new FormControl(''),
    budget: new FormControl(''),
    partitionSize: new FormControl(''),
    partitionLimit: new FormControl('')
  });

  onSubmit() {
    console.log(this.addInstanceForm.controls['symbol'].value);
  }

}
