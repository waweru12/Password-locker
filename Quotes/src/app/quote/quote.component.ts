import { Component, OnInit } from '@angular/core';
import {Quote} from '../quote'




@Component({
  selector: 'app-quote',
  templateUrl: './quote.component.html',
  styleUrls: ['./quote.component.css']
})

export class QuoteComponent implements OnInit {

  Quotes=[
    
    new Quote(1,'Accept responsibility for your life. Know that it is you who will get you where you want to go, no one else.','~ ',new Date(2019,10,14)),
    new Quote(2,'The best decisions aren’t made with your mind, but with your instinct.','~ Lionel Messi',new Date(2018,10,14)),
    new Quote(3,'If you don’t like something, change it. If you can’t change it, change your attitude.','~ Abraham Lincon',new Date(2019,10,14)), 

 ]
 toogleDetails(index){
  this.Quotes[index].showDescription = !this.Quotes[index].showDescription;
}

addNewQuote(quote){
  let quoteLength = this.Quotes.length;
  quote.id=quoteLength+1;
  quote.completeDate = new Date(quote.completeDate)
  this.Quotes.push(quote)
}
  constructor() { }

  ngOnInit() {
  }

}

