import { Component,AfterViewInit, Inject  } from '@angular/core';
import { DataServiceService } from '../Services/data-service.service';
import { TokensService } from '../Services/tokens.service';
import { CommonModule, DOCUMENT, NgForOf } from '@angular/common';
import { FormControl, FormGroup, FormsModule, ReactiveFormsModule } from '@angular/forms';
import { SocketService } from '../Services/socket.service';


@Component({
  selector: 'app-tokens',
  standalone: true,
  imports: [CommonModule,FormsModule,ReactiveFormsModule],
  templateUrl: './tokens.component.html',
  styleUrl: './tokens.component.scss'
})
export class TokensComponent {
  data: any;
  tokens: any;
  socketSubscription: any;
 



  constructor(private dataService: DataServiceService, private tokenService: TokensService, @Inject(DOCUMENT) private document: any,private socket:SocketService) { }
  ngOnInit(): void {
    this.data = this.dataService.getData();
   this.tokenService.generateTokens(this.data).subscribe((data:any) => {
      this.tokens = data;
      console.log(this.tokens);
    });

    

    /* this.tokens = {"sections": [
      {
          "title": "Introduction to Online Education",
          "text": "With the rise of online education in recent years, more and more students are opting to study from the comfort of their own homes rather than attending traditional brick-and-mortar institutions. While online learning can offer numerous benefits, such as flexibility and convenience, it also comes with its own set of challenges. Therefore, to help you succeed in your online studies, here are ten tips to keep in mind:",
          "userInput":"ttt",
          "cta":false,
          "tone":"",
          "writing_style": "",

      },
      {
          "title": "1. Create a dedicated study space",
          "text": "Having a designated area to study can help you focus and minimize distractions. For example, if you have a spare room or home office, you can turn it into your study space. If you don’t have a separate room, you can set up a study area in a quiet corner of your bedroom or living room. The key is to find a space where you can concentrate and be productive.",
          "userInput":"",
          "cta":"",
          "tone":"",
          "writing_style": ""
      }]};
  */
    }

 /*

  showAlert(event: Event, token: any, i: number) {
    event.preventDefault();
    let old_text: string = this.tokens.sections[i].text;
    let f_writing_style: string = this.tokens.sections[i].writing_style;
    let f_content_structure: string = this.tokens.sections[i].content_structure;
    let f_tone: string = this.tokens.sections[i].tone;
    let f_cta: string = this.tokens.sections[i].cta;
    let f_userInput: string = this.tokens.sections[i].userInput;

    this.socket.emit('process-token', {token: old_text, writing_style: f_writing_style,content_structure:f_content_structure,content_tone:f_tone,content_cta:f_cta, userInput: f_userInput});

    const subscription = this.socket.listen('token_response').subscribe((data:any) => {
      console.log(data);
      this.tokens.sections[i].text = data.token;
      this.tokens.sections[i].writing_style = "";
      this.tokens.sections[i].content_structure = "";
      this.tokens.sections[i].tone = "";
      this.tokens.sections[i].cta = "";
      this.tokens.sections[i].userInput = "";
    });

    // For Testing
    console.log(this.tokens.sections[i].text);
    console.log(this.tokens.sections[i].cta);
    console.log(this.tokens.sections[i].title);
    console.log(this.tokens.sections[i].tone);
    console.log(this.tokens.sections[i].writing_style);
    console.log(this.tokens.sections[i].content_structure);


    subscription.unsubscribe();
  }*/



  showAlert(event: Event, token: any, i: number) {
    event.preventDefault();
    let section = { ...this.tokens.sections[i] };

    this.socket.emit('process-token', {
        token: section.text,
        writing_style: section.writing_style,
        content_structure: section.content_structure,
        content_tone: section.tone,
        content_cta: "",
        userInput: section.userInput
    });

    const subscription = this.socket.listen('token_response').subscribe((data: any) => {
        console.log(data);

        // Ensure we are updating the correct section in a safe way
        
            this.tokens.sections[i].text = data.token;
            this.tokens.sections[i].writing_style = "";
            this.tokens.sections[i].content_structure = "";
            this.tokens.sections[i].tone = "";
            this.tokens.sections[i].cta = "";
            this.tokens.sections[i].userInput = "";

            // For Testing
            console.log(this.tokens.sections[i].text);
            console.log(this.tokens.sections[i].cta);
            console.log(this.tokens.sections[i].title);
            console.log(this.tokens.sections[i].tone);
            console.log(this.tokens.sections[i].writing_style);
            console.log(this.tokens.sections[i].content_structure);
        

        // Unsubscribe to prevent memory leaks
        subscription.unsubscribe();
    });
}



}
