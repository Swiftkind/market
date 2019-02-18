import { Component, OnInit } from '@angular/core';
import { CartService } from '../../commons/services/cart/cart.service';
import { ActivatedRoute } from '@angular/router';
import { Title } from '@angular/platform-browser';
import { domain_url } from '../../commons/constants/global.constants';

@Component({
  selector: 'app-cart',
  templateUrl: './cart.component.html',
  styleUrls: ['./cart.component.css']
})
export class CartComponent implements OnInit {
  theme_id:number;
  theme;
  discount;
  dis_price;
  url = domain_url;
  category;

  constructor(
  	private cartService: CartService,
  	private route: ActivatedRoute,
  	private title: Title) { }

  ngOnInit() {
  	this.route.paramMap.subscribe(
  		paramMap =>{
  			this.theme_id = +paramMap.get('id');
  		}
  	);

  	this.themeCart();
  }

  themeCart(){
  	this.cartService.getThemeCart(this.theme_id)
  	.then(
  		response => {
  			this.theme = response;
  			this.title.setTitle('Cart - '+this.theme.name);
  			this.theme.price = this.theme.price.toFixed(2);
  			
  			if(this.theme.discount != null){
  				this.dis_price = this.theme.price * this.theme.discount;
  				this.dis_price = this.theme.price - this.dis_price;
  				this.dis_price = this.dis_price.toFixed(2);
  			}
  			this.discount = +this.theme.discount * 100;
  		}
  	)
  	.catch(
  		error => {
  			return error;
  		}
  	)
  }

  buyTheme(event,theme_id){
    console.log('clicked');
    this.cartService.buyThemeService(theme_id)
    .then(
      response => {
        return response;
      }
    )
    .catch(
      error => {
        return error;
      }
    )
  }

  changeLicense(event,theme_id,license_id){
    this.cartService.editLicenseService(theme_id,license_id)
    .then(
      response => {
        this.themeCart();
        return response;
      }
    )
    .catch(
      error => {
        return error;
      }
    )
  }

  incrementDownload(id){
    console.log('clicked');
    this.cartService.incrementDownloadService(id)
    .then(
      response => {
        console.log(response);
        return response;
      }
    )
    .catch(
      error => {
        return error;
      }
    )
  }



}	
