function verif_2(){
    console.log("verif1")
    var rep1 = document.getElementById("q11");
    var rep2 = document.getElementById("q12");
    var rep3 = document.getElementById("q13");
    var rep4 = document.getElementById("q21");
    var rep5 = document.getElementById("q22");
    var rep6 = document.getElementById("q31");
    var rep7 = document.getElementById("q32");
    var rep8 = document.getElementById("q41");
    var rep9 = document.getElementById("q42");
    var rep10 = document.getElementById("q43");
    var rep11 = document.getElementById("q44");
    var rep12 = document.getElementById("q45");
    var rep13 = document.getElementById("q46");
    var rep14 = document.getElementById("q47");
    var rep15 = document.getElementById("q48");
    
    // ici c'es la réponse n°2, 1 et 2 qui est correcte
    if(rep2.checked==true && rep1.checked==false && rep3.checked==false && rep4.checked==false && rep5.checked==true && rep6.checked==false && rep7.checked==true && rep8.checked==true && rep9.checked==false && rep10.checked==true && rep11.checked==false && rep12.checked==true && rep13.checked==true && rep14.checked==true && rep15.checked==false){
        document.getElementById("texteresult").innerHTML = "Bravo, bonne réponse !";
        setTimeout(function(){window.location.href = "/alarme"}, 500);      
    }
    else{
        document.getElementById("texteresult").innerHTML = "Votre réponse est fausse !"
    }
    //si pas de réponse
    if(rep1.checked==false && rep2.checked==false && rep3.checked==false && rep4.checked==false && rep5.checked==false && rep6.checked==false && rep7.checked==false && rep8.checked==false && rep9.checked==false && rep10.checked==false && rep11.checked==false && rep12.checked==false && rep13.checked==false && rep14.checked==false && rep15.checked==false){
        //alert("Vous devez cocher une case !");
        document.getElementById("texteresult").innerHTML = "Veuillez choisir votre réponse !"
    }
}