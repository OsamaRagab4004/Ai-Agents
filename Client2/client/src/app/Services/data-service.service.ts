import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class DataServiceService {
  private dataArray: any[] = [];

  setData(data: any[]) {
    this.dataArray = data;
  }

  getData() {
    return this.dataArray;
  }

  constructor() { }
}
