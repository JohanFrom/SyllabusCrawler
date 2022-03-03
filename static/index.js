// Check input values and loading 
CheckInput = () => {
    const form = document.forms["search_form"]["search-input"].value
    const numbersInput = document.forms["search_form"]["amount-of-pages"].value


    if(form == ""){
        let error = document.getElementById("error-message-input");
        error.innerHTML = `<span style='color:#C22D39;'> Please enter search values </span>`;
        return false;
    }
    else if(numbersInput == ""){
        let error = document.getElementById("error-message-number");
        error.innerHTML = `<span style='color:#C22D39;'> Must be a number </span>`;
        return false;
    } else if( numbersInput > 15){
        let error = document.getElementById("error-message-number");
        error.innerHTML = `<span style='color:#C22D39;'> Max number is 15</span>`;
        return false;
    }

    document.getElementById("loader").style.display = "block";
}

// Check the scrape result
if(document.URL == "http://127.0.0.1:5000/search"){
    const keyword1 = document.forms["search_form"]["input-keyword1"].value;
    const keyword2 = document.forms["search_form"]["input-keyword2"].value;
    const keyword3 = document.forms["search_form"]["input-keyword3"].value;
    const displayKeywordInfo = document.getElementById("keywordInfo");
    const errorMessage = document.getElementById("error-message");
    const pTag = document.getElementById("scrape-result");

    if(pTag == null || pTag == ""){
        errorMessage.innerHTML = `<span>Fann inget resultat baserat på det som matats in!</span>`;
    } 
    console.log(keyword1);

    if(keyword1 == "" && keyword2 == "" && keyword3 == ""){
        displayKeywordInfo.innerHTML = `<span>Inga nyckelord har angets</span>`;
        errorMessage.innerHTML = `<span>Fann inget resultat baserat på det som matats in!</span>`;
    }else{
        displayKeywordInfo.innerHTML = `<span>Nyckelord:</span>`;
    }
}


