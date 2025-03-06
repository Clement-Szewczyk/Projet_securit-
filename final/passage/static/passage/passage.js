function passage(){
    console.log("passage")
    var rep1 = document.getElementById("alarme").value;
    var rep3 = document.getElementById("porte").value;

    // CODE entre jeu 1 et 2
    if(rep1=="alarme" ){
        document.getElementById("texteresult").innerHTML = "Bravo, bonne réponse !";
        setTimeout(function(){window.location.href = "/alarme"}, 500);
    }
    else{
        document.getElementById("texteresult").innerHTML = "Votre réponse est fausse !"
        //reset des réponses

    }

    // CODE entre jeu 3 et 4
    if(rep3=="porte" ){
        document.getElementById("texteresult").innerHTML = "Bravo, bonne réponse !";
    }
    else{
        document.getElementById("texteresult").innerHTML = "Votre réponse est fausse !"
    }
    
    //si pas de réponse
    if(rep1==("") || rep2==("") ){
        //alert("Vous devez cocher une case !");
        document.getElementById("texteresult").innerHTML = "Veuillez choisir votre réponse !"
    }
}