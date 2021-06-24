function agregar(){
    /*Elementos del formulario */
    var titulo = document.getElementById("titulo");
    var ingredientes = document.getElementById("ingredientes");
    var imagen = document.getElementById("imagen");
    var procedimiento = document.getElementById("procedimiento");
    /*Fin elementos del formulario */

    if(titulo.value!="" && imagen.value!="" && ingredientes.value!="" && procedimiento.value!=""){
        var table = document.createElement("table");
        table.className = "table table-bordered mt-4";

        var tr =  document.createElement("tr");
        var td = document.createElement("td");
        td.setAttribute("colspan", "2");
        td.textContent=titulo.value;
        tr.appendChild(td);

        //INGREDIENTES
        var tr2 =  document.createElement("tr");
        var td2 = document.createElement("td");
        td2.setAttribute("width", "50%");
        td2.textContent=ingredientes.value;
        tr2.appendChild(td2);//INGREDIENTES
        
        //IMAGEN
        var archivo = document.getElementById("imagen").files[0];
        var reader = new FileReader();
        if (archivo) {
            reader.readAsDataURL(archivo);
            reader.onloadend = function () {
                var td3 = document.createElement("td");
                td3.setAttribute("width", "50%");
                td3.setAttribute("align", "center");

                var img = document.createElement("img");
                img.setAttribute("width", "300px");
                img.setAttribute("height", "150px");
                
                img.setAttribute("src", reader.result);
                td3.appendChild(img);
                tr2.appendChild(td3);
            }
        }

        var tr4 =  document.createElement("tr");
        var td4 = document.createElement("td");
        td4.setAttribute("colspan", "2");
        td4.textContent=procedimiento.value;
        tr4.appendChild(td4);


        table.appendChild(tr);
        table.appendChild(tr2);
        table.appendChild(tr4);

        document.getElementById("contenido").appendChild(table);

        titulo.value=""; imagen.value=""; ingredientes.value=""; procedimiento.value="";
        
        $("#exampleModal").modal('hide');
   }

}

function contacto(){
    alert("Gracias por ponerse en contacto con nosotros.");
    location.reload();
}