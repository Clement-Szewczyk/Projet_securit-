function verif_2(){
    var rep1 = document.getElementById("q11");
    var rep2 = document.getElementById("q12"); //TRUE
    var rep3 = document.getElementById("q13");
    var rep4 = document.getElementById("q21"); //TRUE
    var rep5 = document.getElementById("q22");
    var rep6 = document.getElementById("q23");
    var rep7 = document.getElementById("q24"); //TRUE
    var rep8 = document.getElementById("q31");// TRUE
    var rep9 = document.getElementById("q32");// TRUE
    var rep10 = document.getElementById("q33");
    var rep11 = document.getElementById("q34");
    
    
    if(rep2.checked==true && rep1.checked==false && rep3.checked==false && rep4.checked==true && rep5.checked==false && rep6.checked==false && rep7.checked==true && rep8.checked==true && rep9.checked==true && rep10.checked==false && rep11.checked==false){
        document.getElementById("texteresult").innerHTML = "Bravo, bonne réponse !";
        setTimeout(function(){window.location.href = "/evacuation"}, 500);
    }
    else{
        document.getElementById("texteresult").innerHTML = "Votre réponse est fausse !"
    }
    //si pas de réponse
    if(rep1.checked==false && rep2.checked==false && rep3.checked==false && rep4.checked==false && rep5.checked==false && rep6.checked==false && rep7.checked==false && rep8.checked==false && rep9.checked==false && rep10.checked==false && rep11.checked==false){
        //alert("Vous devez cocher une case !");
        document.getElementById("texteresult").innerHTML = "Veuillez choisir votre réponse !"
    }
}