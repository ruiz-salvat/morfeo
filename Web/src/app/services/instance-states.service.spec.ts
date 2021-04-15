import { TestBed } from '@angular/core/testing';

import { InstanceStatesService } from './instance-states.service';

describe('InstanceStatesService', () => {
  let service: InstanceStatesService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(InstanceStatesService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
