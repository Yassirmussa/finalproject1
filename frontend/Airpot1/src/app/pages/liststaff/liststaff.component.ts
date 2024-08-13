import { Component, inject, OnInit } from '@angular/core';
import { StaffService } from '../../services/staff.service';
import { Router } from '@angular/router';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-liststaff',
  templateUrl: './liststaff.component.html',
  styleUrl: './liststaff.component.css'
})
export class ListstaffComponent implements OnInit {
  // constructor(private http:HttpClient){}
  // http = inject(HttpClient)
  data:any
  // private url = String ('http://localhost:8000/api/')

  ngOnInit(): void {
    this.data = [
      {
        'id' :1,
        'name':'HAssan',
        'address':'Muungoni',
        'phone':'077654543'
      }
    ] 
    console.log(this.data);
    
  }

  
  // getAll(){
  //   return this.http.get(this.url+'getstaff').subscribe((data:any)=>{
  //     console.log(data);
      
  //   })
  // }
  
}
