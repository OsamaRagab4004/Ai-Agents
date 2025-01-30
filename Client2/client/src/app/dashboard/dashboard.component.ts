import { Component } from '@angular/core';
import { SummarizedArticlesService } from '../Services/summarized-articles.service';
import { CommonModule, NgForOf } from '@angular/common';

@Component({
  selector: 'app-dashboard',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './dashboard.component.html',
  styleUrl: './dashboard.component.scss'
})
export class DashboardComponent {

  articles: any = [];

  constructor(private summarizedArticlesService: SummarizedArticlesService) { }

  ngOnInit() {
    this.summarizedArticlesService.getData().subscribe({
      next: (data) => {
        this.articles = data;
        console.log(this.articles.result);
      },
      error: (err) => {
        console.error('Error fetching data:', err);
      }
    });
  }

}
