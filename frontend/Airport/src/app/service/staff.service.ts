import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class StaffService {

  private url = String ('http://localhost:8000/api/')

  constructor(private http:HttpClient) { }

  add(){

  }
  
  getAll(){
    return this.http.get(this.url+'getstaff')
  }
  
}
