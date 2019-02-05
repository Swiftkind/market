import { BrowserModule } from '@angular/platform-browser';
import { NgModule, CUSTOM_ELEMENTS_SCHEMA } from '@angular/core';
import { HttpClientModule,HTTP_INTERCEPTORS } from '@angular/common/http';
import { RouterModule, Routes } from "@angular/router";
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { AppRoutingModule } from './app-routing.module';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations'
import { Select2Module } from 'ng2-select2';
import { polyfill } from 'keyboardevent-key-polyfill';
import { TextInputAutocompleteModule } from 'angular-text-input-autocomplete';

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

//Pipes
import { CategoryPipe } from './commons/pipes/category/category.pipe';

//Routes
const routes: Routes = [
  { path: '', component: HomeComponent },
  { path: 'details/:id', component: DetailsComponent },
  { path: 'cart/:id', component: CartComponent },
  { path: 'account', component: AccountComponent }
]

polyfill();

@NgModule({
  declarations: [
    AppComponent,
    HomeComponent,
    CartComponent,
    DetailsComponent,
    AccountComponent,
    CategoryPipe,

  ],
  imports: [
    AccountModule,
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    FormsModule,
    ReactiveFormsModule,
    TextInputAutocompleteModule,
    RouterModule.forRoot(routes, {onSameUrlNavigation: 'reload'}),
  ],
  providers: [
  {
    provide: HTTP_INTERCEPTORS,
    useClass: TokenService,
    multi: true
  }
  ],
  bootstrap: [AppComponent],
  schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class AppModule { }