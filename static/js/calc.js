
function ServiceItem(title, description, price) {
    var self = this;
    self.title = title;
    self.description = description;
    self.price = ko.observable(price);
    //self.quantity = ko.observable(0)
    self.quantity = ko.observable(false); 
}      	
function CalcModel(services) {  
	var self = this;
	self.serv = ko.observableArray([])
	for (var i = 0; i < services.length; i++){
		self.serv.push(new ServiceItem(services[i].title__type, services[i].description, services[i].price))
	}
	self.cost = ko.computed( 
	 function() {
	   var total = 0;
	   for (var i = 0; i < self.serv().length; i++)
	         //total += self.serv()[i].price()*self.serv()[i].quantity()
	   	    self.serv()[i].quantity() ? total += +(self.serv()[i].price()) : total
	   return total;
	} );
	self.clear = function(){
		for (var i = 0; i < self.serv().length; i++)
			self.serv()[i].quantity(false);
	}
}
ko.applyBindings(new CalcModel(services));

