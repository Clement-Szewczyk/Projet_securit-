var image1 = document.getElementById('sucre')
var image2 = document.getElementById('charbon')
var image3 = document.getElementById('chlore')
var image4 = document.getElementById('jerrican')
var image5 = document.getElementById('allumette')
var image6 = document.getElementById('bois')
var image7 = document.getElementById('briquet')
var image8 = document.getElementById('gaz')
var image9 = document.getElementById('oxygène')

image1.addEventListener('dragstart',fonction_dragstart,false);
image1.addEventListener('dragend',fonction_dragend,false);
image2.addEventListener('dragstart',fonction_dragstart,false);
image2.addEventListener('dragend',fonction_dragend,false);
image3.addEventListener('dragstart',fonction_dragstart,false);
image3.addEventListener('dragend',fonction_dragend,false);
image4.addEventListener('dragstart',fonction_dragstart,false);
image4.addEventListener('dragend',fonction_dragend,false);
image5.addEventListener('dragstart',fonction_dragstart,false);
image5.addEventListener('dragend',fonction_dragend,false);
image6.addEventListener('dragstart',fonction_dragstart,false);
image6.addEventListener('dragend',fonction_dragend,false);
image7.addEventListener('dragstart',fonction_dragstart,false);
image7.addEventListener('dragend',fonction_dragend,false);
image8.addEventListener('dragstart',fonction_dragstart,false);
image8.addEventListener('dragend',fonction_dragend,false);
image9.addEventListener('dragstart',fonction_dragstart,false);
image9.addEventListener('dragend',fonction_dragend,false);

function fonction_dragstart(ev){
    document.getElementById('sucre').innerHTML = "déplacement de "+ev.target.id;
    /* on change la transparence de l'élément et on ajoute un cadre */
    this.style.opacity=0.2;
    this.style.borderStyle='dashed';
}

function fonction_dragend(ev){
    ev.preventDefault();
    document.getElementById('sucre').innerHTML = "fin de déplacement de "+ev.target.id;
    /* on remet les valeurs initiales de transparence et on supprime le cadre */
    this.style.opacity=1;
    this.style.borderStyle='none';
}
    
function fonction_dragend(ev){
    ev.preventDefault();
    var id = ev.target.id;
    document.getElementById('sucre').innerHTML="fin de déplacement de "+id;
    /* remettre les valeurs initiales de transparence, supprimer le cadre */
    this.style.opacity=1;
    this.style.borderStyle='none';
}
    
function fonction_dragstart(ev){
    var id = ev.target.id;
    document.getElementById('sucre').innerHTML="déplacement de "+id;
    /* changer transparence de l'élément, ajouter un cadre */
    this.style.opacity=0.2;
    this.style.borderStyle='dashed';
    ev.dataTransfer.setData("Text",ev.target.id);
}    

var cible = document.getElementById('mycart1')
cible.addEventListener('dragover',fonction_dragover,false);
cible.addEventListener('drop',fonction_drop,false);

function fonction_dragover(ev){
    /* empêcher le fonctionnement par défaut */
    ev.preventDefault();
}

var cible = document.getElementById('mycart2')
cible.addEventListener('dragover',fonction_dragover,false);
cible.addEventListener('drop',fonction_drop,false);

function fonction_dragover(ev){
    /* empêcher le fonctionnement par défaut */
    ev.preventDefault();
} 

var cible = document.getElementById('mycart3')
cible.addEventListener('dragover',fonction_dragover,false);
cible.addEventListener('drop',fonction_drop,false);

function fonction_dragover(ev){
    /* empêcher le fonctionnement par défaut */
    ev.preventDefault();
}   

function fonction_drop(ev){
    ev.preventDefault();
    /* récupération de l'identifiant de l'élément déplacé */
    var data=ev.dataTransfer.getData("Text");
    ev.target.appendChild(document.getElementById(data));
}


var rep1 = document.getElementById("sucre");
var rep2 = document.getElementById("charbon");
var rep3 = document.getElementById("chlore");
var rep4 = document.getElementById("jerrican");
var rep5 = document.getElementById("allumette");
var rep6 = document.getElementById("bois");
var rep7 = document.getElementById("briquet");
var rep8 = document.getElementById("gaz");
var rep9 = document.getElementById("oxygène");
var ele = document.getElementById("éléments");
var combustible = document.getElementById("mycart1");
var comburant = document.getElementById("mycart2");
var chaleur = document.getElementById("mycart3");


function verif_éléments(){
    if(ele==0){
        return true
    }
    else{
        return false
    }
}
function verif_combustible(){
    if(combustible==rep1,rep2,rep4,rep5){
        return true
    }
    else{
        return false    
    }
}

function verif_comburant(){
    if(comburant==rep3,rep8,rep9){
        return true
    }
    else{
        return false    
    }
}

function verif_chaleur(){
    if(chaleur==rep6,rep7){
        return true
    }
    else{
        return false    
    }
}

function verif_final(){    
    if(verif_éléments==true){
        if(verif_chaleur==true && verif_comburant==true && verif_combustible==true){
            document.getElementById("texteresult").innerHTML = "Bravo, bonne réponse !";
        }
        else{
            document.getElementById("texteresult").innerHTML = "Votre réponse est fausse !";
        }
    }
    else{
        document.getElementById("texteresult").innerHTML = "Veuillez trier tous les éléments";
    }
}
