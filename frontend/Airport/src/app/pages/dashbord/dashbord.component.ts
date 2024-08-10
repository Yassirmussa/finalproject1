import { Component } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-dashbord',
  templateUrl: './dashbord.component.html',
  styleUrl: './dashbord.component.css'
})
export class DashbordComponent {
  constructor(private router:Router){}
registerStaff() {
  return this.router.navigateByUrl('rf')
}
list: any;

}
