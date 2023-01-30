function verif_1(){
    console.log("verif1")
    var rep1 = document.getElementById("son1");
    var rep2 = document.getElementById("son2");
    var rep3 = document.getElementById("son3");
    var rep4 = document.getElementById("son4");

    // ici c'es la réponse n°2 qui est correcte
    if(rep2.checked==true && rep1.checked==false && rep3.checked==false && rep4.checked==false){
        document.getElementById("texteresult").innerHTML = "Bravo, bonne réponse !";
    }
    else{
        document.getElementById("texteresult").innerHTML = "Votre réponse est fausse !"
    }
    //si pas de réponse
    if(rep1.checked==false && rep2.checked==false && rep3.checked==false && rep4.checked==false){
        //alert("Vous devez cocher une case !");
        document.getElementById("texteresult").innerHTML = "Veuillez choisir votre réponse !"
    }
}



