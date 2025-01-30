import { Injectable } from '@angular/core';
import { HttpClient, HttpClientModule } from '@angular/common/http';


@Injectable({
  providedIn: 'root'
})
export class SummarizedArticlesService {

  constructor(private http: HttpClient) { }

// Get all summarized articles from api ::
  getData() {
    return this.http.get('http://127.0.0.1:8000/summurized_articles/');
  }

  getArticleById(id:string) {
    return this.http.get('http://127.0.0.1:8000/summarized_article_id/?article_id='+id);
  }

  deleteArticleById(id:string) {
    return this.http.get('http://127.0.0.1:8000/delete_summarized_article_id/?article_id='+id);
  }


}
