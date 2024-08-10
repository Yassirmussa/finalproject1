import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
<<<<<<< HEAD
import { MainLayoutComponent } from './layout/main-layout/main-layout.component';
import { DashbordComponent } from './pages/dashbord/dashbord.component';
import { StaffComponent } from './pages/staff/staff.component';
import { LoginComponent } from './pages/login/login.component';
import { RegisterstaffComponent } from './pages/registerstaff/registerstaff.component';


const routes: Routes = [{
  path: '',component:MainLayoutComponent,
  children:[
    {path: 'Dashboard', component:DashbordComponent},
    {path: 'staff', component:StaffComponent},
    {path: 'rf', component:RegisterstaffComponent}
  ]
 
},
{path: 'login', component:LoginComponent}
  
=======
import { NavigationComponent } from './navigation/navigation.component';
import { DashboardComponent } from './pages/dashboard/dashboard.component';
import { StaffComponent } from './pages/staff/staff.component';

const routes: Routes = [
  {path:'', component:NavigationComponent,
    children:[
      
      {path:'staff',component:StaffComponent},
      {path:'dashboard', component:DashboardComponent},
    ]
  },
>>>>>>> 006747c25628b0c05618fc2fbab11453ce2f7ef7
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
