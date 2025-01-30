import { TestBed } from '@angular/core/testing';

import { SummarizedArticlesService } from './summarized-articles.service';

describe('SummarizedArticlesService', () => {
  let service: SummarizedArticlesService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(SummarizedArticlesService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
