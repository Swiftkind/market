import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpClientModule,HTTP_INTERCEPTORS } from '@angular/common/http';
import { RouterModule, Routes } from "@angular/router";
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { AppRoutingModule } from './app-routing.module';

//Service
import { TokenService } from './commons/services/interceptors/token.service';

//Modules
import { AccountModule } from './components/account/account.module';

//Components
import { AppComponent } from './app.component';
import { HomeComponent } from './components/home/home.component';
import { CartComponent } from './components/cart/cart.component';
import { DetailsComponent } from './components/details/details.component';
import { AccountComponent } from './components/account/account.component';

//Routes
const routes: Routes = [
  { path: '', component: HomeComponent },
  { path: 'details', component: DetailsComponent },
  { path: 'cart', component: CartComponent },
  { path: 'account', component: AccountComponent }
]

@NgModule({
  declarations: [
    AppComponent,
    HomeComponent,
    CartComponent,
    DetailsComponent,
    AccountComponent,

  ],
  imports: [
    AccountModule,
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    FormsModule,
    ReactiveFormsModule,
    RouterModule.forRoot(routes, {onSameUrlNavigation: 'reload'}),
  ],
  providers: [
  {
    provide: HTTP_INTERCEPTORS,
    useClass: TokenService,
    multi: true
  }
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }