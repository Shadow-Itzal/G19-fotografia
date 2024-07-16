let closeButton;
function agrandar(img) {
    // Aplica estilos para agrandar la imagen
  
    img.classList.add('agranda');
    if(!closeButton){

        // Crea un botón de cierre para volver a la vista previa
        closeButton = document.createElement('button');
        closeButton.innerText = 'Cerrar';
        closeButton.classList.add('close-button');
        closeButton.onclick = function() {
            
                event.stopPropagation();
                img.classList.remove('agranda');
                console.log(closeButton);
                closeButton.remove(this);
                 closeButton = null;
                
        };
        
        // Agrega el botón de cierre en card
        img.appendChild(closeButton);
    }
    }
    

