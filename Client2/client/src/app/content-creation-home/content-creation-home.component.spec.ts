import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ContentCreationHomeComponent } from './content-creation-home.component';

describe('ContentCreationHomeComponent', () => {
  let component: ContentCreationHomeComponent;
  let fixture: ComponentFixture<ContentCreationHomeComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [ContentCreationHomeComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(ContentCreationHomeComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
