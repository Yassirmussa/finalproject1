import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { StaffService } from '../../services/staff.service';

@Component({
  selector: 'app-staff-list',
  templateUrl: './staff-list.component.html',
  styleUrl: './staff-list.component.css'
})
export class StaffListComponent {
  
  constructor (private staff:StaffService, private router:Router){}
  list: any;
  
    ngOnInit(): void {
      // this.getstaff();
      
    }
  
    // getstaff(){
    //   this.staff.getAll().subscribe((data:any)=>{
    //     this.list = data;
    //     console.table(this.list);
    //   })
    // }
    
registerStaff() {
  return this.router.navigateByUrl('registerStaff')

}


}
