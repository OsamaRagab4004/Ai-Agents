import { Component } from '@angular/core';
import { ReactiveFormsModule } from '@angular/forms';
import { FormControl, FormGroup } from '@angular/forms';
import { DataServiceService } from '../Services/data-service.service';
import { Router } from '@angular/router';


@Component({
  selector: 'app-content-creation-home',
  standalone: true,
  imports: [ReactiveFormsModule],
  templateUrl: './content-creation-home.component.html',
  styleUrl: './content-creation-home.component.scss'
})
export class ContentCreationHomeComponent {

  constructor(private dataService: DataServiceService,private router: Router) { }

  data: any;
  myForm = new FormGroup({
    article_type: new FormControl(''),
    topic: new FormControl(''),
    questions: new FormControl(''),
    tone: new FormControl(''),
    writing_style: new FormControl(''),
    informations: new FormControl(''),

  });


  onSubmit() {
    this.data = this.myForm.value;
    this.dataService.setData(this.data);
    this.router.navigate(['/tokens']);
    
  } 
}
