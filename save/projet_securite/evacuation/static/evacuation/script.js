function verif_2(){
    console.log("verif1")
    var rep1 = document.getElementById("q11");
    var rep2 = document.getElementById("q12");
    var rep3 = document.getElementById("q13");
    var rep4 = document.getElementById("q21");
    var rep5 = document.getElementById("q22");
    var rep6 = document.getElementById("q31");
    var rep7 = document.getElementById("q32");
    var rep8 = document.getElementById("q33");
    var rep9 = document.getElementById("q34");
    
    
    // ici c'es la réponse n°2, 1 et 2 qui est correcte
    if(rep2.checked==false && rep1.checked==true && rep3.checked==false && rep4.checked==false && rep5.checked==true && rep6.checked==false && rep7.checked==false && rep8.checked==false && rep9.checked==true){
        document.getElementById("texteresult").innerHTML = "Bravo, bonne réponse !";
    }
    else{
        document.getElementById("texteresult").innerHTML = "Votre réponse est fausse !"
    }
    //si pas de réponse
    if(rep1.checked==false && rep2.checked==false && rep3.checked==false && rep4.checked==false && rep5.checked==false && rep6.checked==false && rep7.checked==false && rep8.checked==false && rep9.checked==false){
        //alert("Vous devez cocher une case !");
        document.getElementById("texteresult").innerHTML = "Veuillez choisir votre réponse !"
    }
}