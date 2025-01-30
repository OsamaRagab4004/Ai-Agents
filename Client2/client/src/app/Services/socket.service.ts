import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import io from 'socket.io-client';


@Injectable({
  providedIn: 'root'
})

export class SocketService {

  private socket: any;

  constructor() { 
    this.socket = io('http://localhost:8000'); // URL of the FastAPI server
  }

  listen(eventName: string): Observable<any> {
    return new Observable((subscriber) => {
      this.socket.on(eventName, (data: any) => {
        subscriber.next(data);
      });
    });
  }

  emit(eventName: string, data: any): void {
    this.socket.emit(eventName, data);
  }
}
