import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { LoginComponent } from './components/login/login.component';
import { ReactiveFormsModule } from '@angular/forms';
import { ScrollingModule } from '@angular/cdk/scrolling';
import { HomeComponent } from './components/home/home.component';
import { appRoutingModule } from './app.routing';
import { ContainerComponent } from './components/container/container.component';
import { InstancesComponent } from './components/instances/instances.component';
import { AddInstanceComponent } from './components/add-instance/add-instance.component';
import { DashboardComponent } from './components/dashboard/dashboard.component';
import {MatIconModule} from '@angular/material/icon';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { LineChartComponent } from './components/line-chart/line-chart.component';
import { HttpClientModule } from '@angular/common/http';
import { API_BASE_URL } from './injection-tokens/api-base-url-token';
import { LogsComponent } from './components/logs/logs.component';

@NgModule({
  declarations: [
    AppComponent,
    LoginComponent,
    HomeComponent,
    ContainerComponent,
    InstancesComponent,
    AddInstanceComponent,
    DashboardComponent,
    LineChartComponent,
    LogsComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    ReactiveFormsModule,
    MatIconModule,
    ScrollingModule,
    appRoutingModule,
    BrowserAnimationsModule,
    HttpClientModule
  ],
  providers: [
    {provide: API_BASE_URL, useValue: 'http://localhost:5000/'}
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
