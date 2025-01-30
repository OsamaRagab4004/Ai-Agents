import { Injectable } from '@angular/core';
import { HttpClient, HttpClientModule } from '@angular/common/http';


@Injectable({
  providedIn: 'root'
})
export class TokensService {

  constructor(private http: HttpClient) { }
  generateTokens(data: any) {
    const baseUrl = 'http://127.0.0.1:8000/process-article/';
    const queryParams = `?article_type=${encodeURIComponent(data.article_type)}&general_topic=${encodeURIComponent(data.topic)}&tone=${encodeURIComponent(data.tone)}&writing_style=${encodeURIComponent(data.writing_style)}&questions=${encodeURIComponent(data.questions)}&information=${encodeURIComponent(data.information)}`;
    const fullUrl = baseUrl + queryParams;
    return this.http.post(fullUrl, data);
  
  }

// http://127.0.0.1:8000/process-article/?article_type=blog post&general_topic=10 tips about starting your own shop as business &tone=Informative&writing_style=Professional and Persuasive&questions=Is it better to study online from home or from another place ? how to organize the time ? how to save money going to university and learn everything from internet&information=


}
