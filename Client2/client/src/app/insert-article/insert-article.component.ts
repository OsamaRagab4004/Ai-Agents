import { Component } from '@angular/core';
import { SocketService } from '../Services/socket.service';
@Component({
  selector: 'app-insert-article',
  standalone: true,
  imports: [],
  templateUrl: './insert-article.component.html',
  styleUrl: './insert-article.component.scss'
})
export class InsertArticleComponent {

  constructor(private socketService: SocketService) {}
  message:any = 'Test';
  url:string = 'https://newsroom.deatch.paypal-corp.com/blog?o=0';
  first_page:number = 0;
  last_page:number = 10;
  website_id:String = 'Chargebee';
  increament:number = 10;


  /**
   * Sends a message using the socket service.
   * Emits the message 'Hello from Angular' through the socket service and listens for the 'message' event.
   * When a message is received, it logs the data to the console.
   */
  async sendMessage(): Promise<void> {
    await this.socketService.emit('scrap', {
      url: this.url,
      first_page: this.first_page,
      last_page: this.last_page,
      increament: this.increament
    });
    await this.socketService.listen('scrap_result').subscribe((data: any) => {
      console.log(data);
      this.message = data;
    });
  }

}
