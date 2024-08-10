import { NgModule } from '@angular/core';
import { BrowserModule, provideClientHydration } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { provideAnimationsAsync } from '@angular/platform-browser/animations/async';
<<<<<<< HEAD
=======
import { NavigationComponent } from './navigation/navigation.component';
>>>>>>> 006747c25628b0c05618fc2fbab11453ce2f7ef7
import { MatToolbarModule } from '@angular/material/toolbar';
import { MatButtonModule } from '@angular/material/button';
import { MatSidenavModule } from '@angular/material/sidenav';
import { MatIconModule } from '@angular/material/icon';
import { MatListModule } from '@angular/material/list';
<<<<<<< HEAD
import { MainLayoutComponent } from './layout/main-layout/main-layout.component';
import { DashbordComponent } from './pages/dashbord/dashbord.component';
import { StaffComponent } from './pages/staff/staff.component';
import { LoginComponent } from './pages/login/login.component';
import { MatCardModule } from '@angular/material/card';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';
import { ReactiveFormsModule } from '@angular/forms';
import { RegisterstaffComponent } from './pages/registerstaff/registerstaff.component';



=======
import { DashboardComponent } from './pages/dashboard/dashboard.component';
import { StaffComponent } from './pages/staff/staff.component';
>>>>>>> 006747c25628b0c05618fc2fbab11453ce2f7ef7

@NgModule({
  declarations: [
    AppComponent,
<<<<<<< HEAD
    MainLayoutComponent,
    DashbordComponent,
    StaffComponent,
    LoginComponent,
    RegisterstaffComponent,
=======
    NavigationComponent,
    DashboardComponent,
    StaffComponent
>>>>>>> 006747c25628b0c05618fc2fbab11453ce2f7ef7
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    MatToolbarModule,
    MatButtonModule,
    MatSidenavModule,
    MatIconModule,
<<<<<<< HEAD
    MatListModule,
    ReactiveFormsModule,
    MatInputModule,
    MatFormFieldModule,
    MatCardModule,
=======
    MatListModule
>>>>>>> 006747c25628b0c05618fc2fbab11453ce2f7ef7
  ],
  providers: [
    provideClientHydration(),
    provideAnimationsAsync()
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
