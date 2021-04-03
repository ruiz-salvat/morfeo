import { Component, OnInit } from '@angular/core';
import { FormControl, FormGroup, ReactiveFormsModule } from '@angular/forms';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {

  constructor() { }

  ngOnInit(): void {
  }

  loginForm = new FormGroup({
    username: new FormControl(''),
    password: new FormControl('')
  });
  
  onSubmit() {
    // TODO: Authenticate
    console.log("username: " + this.loginForm.controls["username"].value);
    console.log("password: " + this.loginForm.controls["password"].value);
  }
}
