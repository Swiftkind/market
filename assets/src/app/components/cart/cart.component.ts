import { Component, OnInit } from '@angular/core';
import { CartService } from '../../commons/services/cart/cart.service';
import { ActivatedRoute } from '@angular/router';
import { Title } from '@angular/platform-browser';

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



}	
