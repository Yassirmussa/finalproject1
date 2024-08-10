import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { DashbordComponent } from './pages/dashbord/dashbord.component';
import { MainLayoutComponent } from './layout/main-layout/main-layout.component';
import { StaffListComponent } from './pages/staff-list/staff-list.component';
import { RegisterStaffComponent } from './pages/register-staff/register-staff.component';

const routes: Routes = [{
  path: '',component:MainLayoutComponent,
  children: [
    {path: 'dashbord',component:DashbordComponent},
    {path: 'staffList', component:StaffListComponent},
    {path: 'registerStaff', component:RegisterStaffComponent}
  ]
}];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
