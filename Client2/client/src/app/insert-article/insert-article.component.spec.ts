import { ComponentFixture, TestBed } from '@angular/core/testing';

import { InsertArticleComponent } from './insert-article.component';

describe('InsertArticleComponent', () => {
  let component: InsertArticleComponent;
  let fixture: ComponentFixture<InsertArticleComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [InsertArticleComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(InsertArticleComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
