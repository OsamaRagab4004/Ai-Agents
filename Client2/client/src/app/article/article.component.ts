import { Component, ElementRef, Renderer2 } from '@angular/core';
import { SummarizedArticlesService } from '../Services/summarized-articles.service';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-article',
  standalone: true,
  imports: [],
  templateUrl: './article.component.html',
  styleUrl: './article.component.scss'
})
export class ArticleComponent {
  constructor(private summarizedArticlesService: SummarizedArticlesService, private activatedRoute: ActivatedRoute,private el: ElementRef, private renderer: Renderer2) { }
  article: any = [];
  userId: string = '';

  ngOnInit() {
    this.userId = this.activatedRoute.snapshot.params['articleId'];
    this.summarizedArticlesService.getArticleById(this.userId).subscribe({
      next: (data) => {
        this.article = data;
        console.log(this.article.result);
      },
      error: (err) => {
        console.error('Error fetching data:', err);
      }
    });
  }

  afterViewInit() {
    const specificElement = this.el.nativeElement.querySelector('h2');
    if (specificElement) {
      this.renderer.setStyle(specificElement, 'color', 'red');
    }

  }


  deleteArticle() {
    let id = this.userId;
    this.summarizedArticlesService.deleteArticleById(id).subscribe({
      next: (data) => {
        alert("Deleted Successfully");
      },
      error: (err) => {
        console.error('Error fetching data:', err);
      }
    });
  }

}
