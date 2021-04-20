import { TestBed } from '@angular/core/testing';
import { InstanceDetailsService } from './instance-details.service';

describe('InstanceDetailsService', () => {
  let service: InstanceDetailsService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(InstanceDetailsService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
