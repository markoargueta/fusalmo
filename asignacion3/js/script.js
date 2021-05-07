//LLAMANDO LA HORA CON LA FUNCION hora().
setInterval(hora, 1000);

function agregar(){
     /*Elementos del formulario */
     var codigo = document.getElementById("codigo");
     var elemento = document.getElementById("elemento");
     var costo = document.getElementById("costo");
     var fecha = document.getElementById("fecha");
     /*Fin elementos del formulario */
     var arreglo = [codigo, elemento, costo, fecha];
     
     if(codigo.value!="" && elemento.value!="" && costo.value!="" && fecha.value!=""){

     var acumulador = Number(document.getElementById("totalCosto").textContent);
     var auxiliar = 0;

     var elementos = Number(document.getElementById("totalElementos").textContent);

     var arreglo = [codigo, elemento, costo, fecha];
    
     //CREACIÓN DE ELEMENTOS DE LA TABLA.
     var table = document.getElementById('mitabla');
     var tr = document.createElement("tr");

     for (let i = 0; i <=3; i++) {
        var td = document.createElement("td");
        td.textContent=arreglo[i].value;
        auxiliar+=arreglo[2].value/3;
        tr.appendChild(td);
        arreglo[i].value="";//LIMPIA EL FORMULARIO.
         
     }
     acumulador+=auxiliar;
     elementos+=1;

     //BOTONES DE OPCIONES.
     var editar = document.createElement("td");
     editar.innerHTML="<button onclick='editar(this)' class='btn btn-link'>Editar</button>";
     var eliminar = document.createElement("td");
     eliminar.innerHTML="<button onclick='eliminar(this)' class='btn btn-link'>Eliminar</button>";
     tr.appendChild(editar);
     tr.appendChild(eliminar);
     //FIN BOTONES DE OPCIONES.
     

     table.appendChild(tr); //FIN CREACIÓN DE ELEMENTOS DE LA TABLA.

     document.getElementById("totalCosto").innerHTML=acumulador;
     document.getElementById("totalElementos").innerHTML=elementos;
    
    }    

}

function eliminar(t){
    var confirmar = confirm("¿Seguro que desea eliminar?");
    if(confirmar)
    {
    var td = t.parentNode;
    var tr = td.parentNode;
    var table = tr.parentNode;

    //RESTAR EL COSTO
    var restar = Number(td.previousSibling.previousSibling.previousSibling.textContent);
    var costo = Number(document.getElementById("totalCosto").textContent);
    document.getElementById("totalCosto").innerHTML=costo-restar;
    //FIN RESTAR EL COSTO

    //RESTAR ELEMENTOS.
    var elementos = Number(document.getElementById("totalElementos").textContent);
    document.getElementById("totalElementos").innerHTML=elementos-1;
     //FIN RESTAR ELEMENTOS.
   
    table.removeChild(tr);
    }
    else{
        alert("No eliminado");
    }
}

function editar(t){
    var td = t.parentNode;
    //VARIABLES PARA OBTENER VALOR DE TD.
    var codAntiguo = td.previousSibling.previousSibling.previousSibling.previousSibling.textContent;
    var elemAntiguo = td.previousSibling.previousSibling.previousSibling.textContent;
    var costoAntiguo = td.previousSibling.previousSibling.textContent;
    var fechaAntiguo = td.previousSibling.textContent;

    alert ("Si no desea modificar los elementos deje vacía la ventana.")

    //SOLICITANDO LOS NUEVOS DATOS.



    //SOLICITANDO NUEVO CÓDIGO.
    var codigo = prompt("Escriba el nuevo código: ");
    if(codigo=="" || codigo==undefined){//SINO ESCRIBEN EN LA VENTANA QUEDA EL VALOR SIN MODIFICAR.
    td.previousSibling.previousSibling.previousSibling.previousSibling.textContent = codAntiguo;
    }
    else{
    td.previousSibling.previousSibling.previousSibling.previousSibling.textContent = codigo;
    }//FIN SOLICITANDO NUEVOCÓDIGO.


    
    //SOLICITANDO NUEVO ELEMENTO (PRODUCTO).
    var elemento = prompt("Escriba el nuevo elemento: ");
    if(elemento=="" || elemento==undefined){//SINO ESCRIBEN EN LA VENTANA QUEDA EL VALOR SIN MODIFICAR.
    td.previousSibling.previousSibling.previousSibling.textContent = elemAntiguo;
    }
    else{
    td.previousSibling.previousSibling.previousSibling.textContent = elemento;
    }//FIN SOLICITANDO NUEVO ELEMENTO (PRODUCTO).



    //ALMACENAMOS EL COSTO ANTES DE MODIFICARLO.
    var costoviejo = Number(document.getElementById("totalCosto").textContent);

    //SOLICITANDO NUEVO COSTO.
    var costo = prompt("Escriba el nuevo costo: ");
    if(costo=="" || costo==undefined){//SINO ESCRIBEN EN LA VENTANA QUEDA EL VALOR SIN MODIFICAR.
    td.previousSibling.previousSibling.textContent = costoAntiguo;
    }
    else{
    td.previousSibling.previousSibling.textContent = costo;
    
    //RESTAR EL COSTO
    var elementos = Number(document.getElementById("totalElementos").textContent);    

    //VALIDANDO EN CASO QUE SOLO HAYA UN ELEMENTO.
    if(elementos==1){
        //SIMPLEMENTE DEJAMOS EL NUEVO VALOR.
        document.getElementById("totalCosto").innerHTML=Number(costo);
    }
    else //SI HAY MAS DE UN ELEMENTO.
    {
        document.getElementById("totalCosto").innerHTML=(Number(costo)+costoviejo-costoAntiguo);
    }
    
    //FIN RESTAR EL COSTO
    }//FIN SOLICITANDO NUEVO COSTO.



    //SOLICITANDO NUEVO FECHA.
    var fecha = prompt("Escriba la nueva fecha (dd-mm-aaaa): ");
    if(fecha==""|| fecha==undefined){//SINO ESCRIBEN EN LA VENTANA QUEDA EL VALOR SIN MODIFICAR.
    td.previousSibling.textContent = fechaAntiguo;
    }
    else{
    td.previousSibling.textContent = fecha;
    }
    //FIN SOLICITANDO NUEVO FECHA.

}

function hora(){
    var d = new Date();
    document.getElementById("horaActual").innerHTML='Fecha: ' + d.getDate() + "/" + (d.getMonth()+1) + "/"  + d.getFullYear() + " Hora: " + d.getHours() + ":"+d.getMinutes()+ ":" +d.getSeconds();
}