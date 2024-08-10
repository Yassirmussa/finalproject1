import { Component, OnInit } from '@angular/core';
import { StaffService } from '../../service/staff.service';
<<<<<<< HEAD
import { Router } from '@angular/router';
=======
>>>>>>> 006747c25628b0c05618fc2fbab11453ce2f7ef7

@Component({
  selector: 'app-staff',
  templateUrl: './staff.component.html',
  styleUrl: './staff.component.css'
})
export class StaffComponent implements OnInit {

<<<<<<< HEAD
  constructor (private staff:StaffService, private router:Router){}
list: any;

  ngOnInit(): void {
    this.getstaff();
=======
  list:any

  constructor(private staff:StaffService){}

  ngOnInit(): void {
>>>>>>> 006747c25628b0c05618fc2fbab11453ce2f7ef7
    
  }

  getstaff(){
    this.staff.getAll().subscribe((data:any)=>{
<<<<<<< HEAD
      this.list = data;
      console.table(this.list);
    })
  }
  registerStaff(){
    return this.router.navigateByUrl("rf");
=======
      console.log(data);
      
    })
  }

  updateStaff(Sid:any){

  }

  deleteStaff(Sid:any){

>>>>>>> 006747c25628b0c05618fc2fbab11453ce2f7ef7
  }

}
