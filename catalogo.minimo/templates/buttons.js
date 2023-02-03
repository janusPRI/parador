<script language="Javascript" >
var current_parent='todos'
var current_child='all'

// window.addEventListener("hashchange", function() { scrollBy(0, 250) })

function sendCart(text) {
    printCart();

  var parador = document.getElementsByClassName("parador");
  if(parador){
  var fecha  = document.getElementById("fecha-inicio").value;
  fecha="\n* Fecha: "+fecha+"\n"
  }else{
    fecha=""
  }

    var element = document.createElement('a');
    var texto=encodeURIComponent("Reserva en Janus\n"+ fecha+ text);
    var http="http://wa.me/"+ {{ xx.WHATSAPPNUM }} +"?text=" + texto
    element.setAttribute('href',http );
    element.setAttribute('target',"_blank");
    element.style.display = 'none';
    document.body.appendChild(element);

    element.click();

    document.body.removeChild(element);
}


var userSelection = document.getElementsByClassName('sendCarts');

for(var i = 0; i < userSelection.length; i++) {
  (function(index) {
    userSelection[index].addEventListener("click", function() {

    var text =createCart()
    var oldWord="<br "
    var reg = new RegExp("<br />", "g");
    var newtext=text.replace(reg, "\r\n");  
    sendCart(newtext);
     },false)
  })(i);
}

var userSelection = document.getElementsByClassName('resetCarts');

for(var i = 0; i < userSelection.length; i++) {
  (function(index) {
    userSelection[index].addEventListener("click", resetCart,false)
  })(i);
}

var userSelection = document.getElementsByClassName('searchOptions');

for(var i = 0; i < userSelection.length; i++) {
  (function(index) {
    userSelection[index].addEventListener("click", showAll('b-parent','c-parent'),false)
  })(i);
}

function showId(myid) {
  current_parent=myid
  // console.log('showid: '+current_parent)
  let x0 = document.getElementById(myid);
  x0.style.display = "block";
}

function showCarretById(myid) {
  showId(myid+'-content')
  caretDownById(myid+'-caret')
}

function caretDownById(myid) {
  let x = document.getElementById(myid);
    x.className = x.className.replace(" caret-down", "");
    x.className = x.className.replace(" caret", "");
    x.className += " caret";
}


function caretUp(myclass) {
  let i, x = document.getElementsByClassName(myclass);
  for (i = 0; i < x.length; i++) {
    x[i].className = x[i].className.replace(" caret-down", "");
    x[i].className = x[i].className.replace(" caret", "");
    x[i].className += " caret-down";
  }
}

function caretDown(myclass) {
  let i, x = document.getElementsByClassName(myclass);
  for (i = 0; i < x.length; i++) {
    x[i].className = x[i].className.replace(" caret-down", "");
    x[i].className = x[i].className.replace(" caret", "");
    x[i].className += " caret";
  }
}

function showClass(myclass) {
  let i, x = document.getElementsByClassName(myclass);
  for (i = 0; i < x.length; i++) {
    x[i].style.display = "block";
  }
}

function toggleByClass(myclass) {
  let i, x = document.getElementsByClassName(myclass);

  for (i = 0; i < x.length; i++) {
    if (x[i].style.display === "none") {
      x[i].style.display = "block";
    } else {
      x[i].style.display = "none";
    }
  }
}

function toggleById(myid) {
  let x0 = document.getElementById(myid);
  if (x0.style.display === "none") {
    x0.style.display = "block";
  } else {
    x0.style.display = "none";
  }
}

function showAll(mylinks,myclass) {

  current_parent='todos'

  showClass(myclass);

  // saco el sombreado de los botones
  let i,tablinks = document.getElementsByClassName(mylinks);
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].className = tablinks[i].className.replace(" w3-red", "");
  }

  caretDown('parent-caret');
  showClass('parent-content');

}



  showClass('parent-content');
  toggleByClass('parent-content');
  caretUp('parent-caret');

function expandCard(myid,myclass) {

  var x0 = document.getElementById(myid);
  if (x0.style.display === "none") {
    x0.style.display = "block";
  } else {
    x0.style.display = "none";
  }

  x = document.getElementsByClassName(myclass);

  for (i = 0; i < x.length; i++) {
    if(x[i]!=x0){
    x[i].style.display = "none";
    }
  }
}

function openParents(evt, myid,mylinks,myclass) {
  
  current_parent=myid

  var i, x, x0,tablinks;
  x0=document.getElementById(myid);
  x = document.getElementsByClassName(myclass);

  var showingall=1;

  for (i = 0; i < x.length; i++) {

    if (x[i].style.display === "none") {
      showingall=0;
    }

    if(x[i]!=x0){
    x[i].style.display = "none";
    }
  }


  tablinks = document.getElementsByClassName(mylinks);
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].className = tablinks[i].className.replace(" w3-red", "");
  }

  if(showingall===0){
  if (x0.style.display === "none") {
    x0.style.display = "block";
    evt.currentTarget.className += " w3-red";
  } else {
    x0.style.display = "none";
  }
  }else{
    evt.currentTarget.className += " w3-red";
  }

  showCarretById(myid)
  // document.getElementById(myid).style.display = "block";
}

function addToCart(idNAME){
  var myelement = document.getElementById(idNAME);
  // var cantidad = myelement.value
  // console.log(cantidad)
  myelement.value++
// var cantidad = myelement.value
  // console.log(cantidad)
  printCart();
}

function removeFromCart(idNAME){
  var myelement = document.getElementById(idNAME);
  if(myelement.value>0){
  myelement.value--;
  printCart();
  }
}

function createCart(){
// var x = document.querySelectorAll(".intro");
// document.getElementById("demo").innerHTML = 
// 'The first paragraph (index 0) with class="intro": ' + x[0].innerHTML;  
  var myclass;
  myclass = document.getElementsByClassName("cantidad");
//  console.log(myclass)
  const now = new Date();
  var month =now.getUTCMonth()+1
  var text = "";//now.getUTCFullYear()+"-"+month+"-"+now.getUTCDate()+"\n\n";
  var preciototal=0,cantidadtotal=0;
  for (var i = 0; i < myclass.length ;i++) {    
    var cantidad=myclass[i].value; //encodeURIComponent(myclass[i].value)
    var name=myclass[i].name
    var myid=name+"-price"

    var myid_var=name+"-var"
    var aux=name.split("/");
    // console.log(name);
    // console.log(aux);
    var productname=aux[aux.length-1];

    // console.log(productname);
    myarticle = document.getElementById(myid);


//    text += x.elements[i].value + "<br>";
  if(cantidad>0){
    var precio_vec=myarticle.value.split("|"); //encodeURIComponent(myarticle.value)
    // console.log(precio_vec)

    var price_index=0;

    myvar = document.getElementById(myid_var);
    if(myvar){
    if(myvar.value>precio_vec.length){
      myvar.value=precio_vec.length
    }
    price_index=myvar.value-1;
    }
    var precio=precio_vec[price_index];

    cantidadtotal=cantidadtotal+parseInt(cantidad);
    preciototal+=(cantidad*precio);
    //text += "("+ cantidad + ") "+ name + ": ["+ cantidad + " x $"+ precio +"] <br />";
    // text +=  "* "+ name + ": ["+ cantidad + " x $"+ precio +"] \n";
     text +=  "* "+ productname + ": ["+ cantidad + " x $"+ precio +"] \n";
  }
  
  }

  var visitantes = document.getElementsByClassName("visitantes");
  var visitan=0
  for (var i = 0; i < visitantes.length ;i++) {    
    var cantidad=visitantes[i].value;
    var name=visitantes[i].name
    var myvar=name+"-var"
    my_visitante = document.getElementById(myvar);
    visitan+=parseInt(my_visitante.value);
  }
  if(visitan>0){
      text += "\nCant. de visitantes: "+visitan
  }
  
  pasajeros = document.getElementsByClassName("pasajeros");
  var duermen=0
  for (var i = 0; i < pasajeros.length ;i++) {    
    var cantidad=pasajeros[i].value;
    var name=pasajeros[i].name
    var myid=name+"-cant"
    my_noche = document.getElementById(myid);

    if(my_noche.value>=1){
      var myvar=name+"-var"
      my_pasajero = document.getElementById(myvar);
      duermen+=parseInt(my_pasajero.value);
    }
  }
  if(duermen>0){
      text += "\nCant. de personas: "+duermen
  }



  parador = document.getElementsByClassName("parador");
  var costodeenvio=0;
  if(parador){
  // text += "\nCant. de productos: "+cantidadtotal

  // if(cantidadtotal>0){  
  //   if(xx.COSTODEENVIO>0){
  //   // text+="\n";
  //   costodeenvio=600  
  //   preciototal+=costodeenvio
  //   text += "\nCosto de envio: $"+costodeenvio+"\n"
  //   }
  // }

  // var fecha  = document.getElementById("fecha-inicio").value;
  // fecha="\nFecha llegada: "+fecha+"\n"
  }else{
    // fecha=""
  }
    // return text += "<br /><br /> Importe total: $"+ preciototal+" <br /><br />";
    return text += "\nImporte total: $"+ preciototal+"\n";
}

function printCart(){
  var text=createCart()
  // document.getElementById("carrito").innerHTML = text;
  // document.getElementById("carrito").value = text;
  // textAreaAdjust(document.getElementById('carrito') );

  var pedidos=document.getElementsByClassName("pedido")
  for (var i = 0; i < pedidos.length ;i++) { 
    pedidos[i].value = text;
   textAreaAdjust(pedidos[i]);
  }
  
  
}


window.addEventListener('load', printCart() )
//window.onload=printCart;

function resetCart(){
  // var text=createCart()
  // // document.getElementById("carrito").innerHTML = text;
  // document.getElementById("carrito").value = "";
  // textAreaAdjust(document.getElementById('carrito') );
  var myclass,i;
  myclass = document.getElementsByClassName("cantidad");
  for (i = 0; i < myclass.length ;i++) { 
    myclass[i].value="0"
    myclass[i].placeholder="0"
  }
    myclass = document.getElementsByClassName("pasajeros");
  for (i = 0; i < myclass.length ;i++) { 
    myclass[i].value="1"
    myclass[i].placeholder="1"
  }

  var text=createCart()
  

  // document.getElementById("carrito").value = text;
  // textAreaAdjust(document.getElementById('carrito') );
  var pedidos=document.getElementsByClassName("pedido")
  for (var i = 0; i < pedidos.length ;i++) { 
    pedidos[i].value = text;
   textAreaAdjust(pedidos[i]);
  }
}

// $(document).ready(function(){

//   textAreaAdjust(document.getElementById('carrito') );
// });

function textAreaAdjust(o) {
  o.style.height = "1px";
  o.style.height = (o.scrollHeight)+"px";
  // o.style.width = "1px";
  // o.style.width = (o.scrollWidth)+"px";
}


var toggler = document.getElementsByClassName("caret");
var i;

for (i = 0; i < toggler.length; i++) {
  toggler[i].addEventListener("click", function() {
    // this.parentElement.querySelector(".nested").classList.toggle("active");
    this.classList.toggle("caret-down");
  });
} 


var close = document.getElementsByClassName("close-details");

for (let i = 0; i < close.length; i++) {
  close[i].addEventListener("click", function() {
    let pedidos = document.getElementsByClassName("details");
      for (let j = 0; j < pedidos.length; j++) {
        pedidos[j].style.display = "none";
    }
  });
} 
</script>