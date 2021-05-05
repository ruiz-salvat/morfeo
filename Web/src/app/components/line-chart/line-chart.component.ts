import { Component, ElementRef, OnInit } from '@angular/core';
import * as d3 from 'd3';
import { DashboardService } from '../../services/dashboard.service';

@Component({
  selector: 'app-line-chart',
  templateUrl: './line-chart.component.html',
  styleUrls: ['./line-chart.component.css']
})
export class LineChartComponent implements OnInit {

  private width = 400;
  private height = 400;
  private margin = 25;
  public svg;
  public svgInner;
  public yScale;
  public xScale;
  public xAxis;
  public yAxis;
  public lineGroup;

  public constructor(
    public chartElem: ElementRef,
    private dashboardService: DashboardService) {}

  ngOnInit(): void {
    this.dashboardService.getChartObservable().subscribe(trades => {
      let data: { value: number, date: string }[] = [];
      let cumulativeGains = 0;
      trades.forEach(t => {
        if (t.operation == "SELL") {
          cumulativeGains = cumulativeGains + t.gain;
          let tradeData = {
            "value": cumulativeGains,
            "date": t.time
          }
          data.push(tradeData);
        }
      });
      this.initializeChart(data);
      this.drawChart(data);
      window.addEventListener('resize', () => this.drawChart(data));
    });
  }

  initializeChart(data: { value: number, date: string }[]) {
    this.svg = d3
    .select(this.chartElem.nativeElement)
    .select('.linechart')
    .append('svg')
    .attr('height', this.height);

    this.svgInner = this.svg
    .append('g')
    .style('transform', 'translate(' + this.margin + 'px, ' + this.margin + 'px)');

    this.yScale = d3
      .scaleLinear()
      .domain([d3.max(data, d => d.value) + 1, d3.min(data, d => d.value) - 1])
      .range([0, this.height - 2 * this.margin]);
    this.xScale = d3.scaleTime().domain(d3.extent(data, d => new Date(d.date)));

    this.yAxis = this.svgInner
      .append('g')
      .attr('id', 'y-axis')
      .style('transform', 'translate(' + this.margin + 'px, 0)');
    this.xAxis = this.svgInner
      .append('g')
      .attr('id', 'x-axis')
      .style('transform', 'translate(0, ' + (this.height - 2 * this.margin) + 'px)');

    this.lineGroup = this.svgInner
      .append('g')
      .append('path')
      .attr('id', 'line')
      .style('fill', 'none')
      .style('stroke', 'white')
      .style('stroke-width', '2px');
  }

  drawChart(data: { value: number, date: string }[]) {
    this.width = this.chartElem.nativeElement.getBoundingClientRect().width;
    this.svg.attr('width', this.width);

    this.xScale.range([this.margin, this.width - 2 * this.margin]);
    const xAxis = d3
      .axisBottom(this.xScale)
      .ticks(10)
      .tickFormat(d3.timeFormat('%d / %m / %Y'));
    this.xAxis.call(xAxis);
    const yAxis = d3
      .axisRight(this.yScale);
    this.yAxis.call(yAxis);

    const line = d3
      .line()
      .x(d => d[0])
      .y(d => d[1])
      .curve(d3.curveMonotoneX);
    const points: [number, number][] = data.map(
      d => [this.xScale(new Date(d.date)), this.yScale(d.value)]
    );
    this.lineGroup.attr('d', line(points));
  }

}
