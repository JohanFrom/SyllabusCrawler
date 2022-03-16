// Check input values and loading 
CheckInput = () => {
    let serachInput = document.forms["search_form"]["search-input"].value
    let numbersInput = Number(document.forms["search_form"]["amount-of-pages"].value)
    let keyword1 = document.forms["search_form"]["input-keyword1"].value;
    let keyword2 = document.forms["search_form"]["input-keyword2"].value;
    let keyword3 = document.forms["search_form"]["input-keyword3"].value;
    let displayKeywordInfo = document.getElementById("keywordInfo");
    let errorInput = document.getElementById("error-message-input");
    let errorNumber = document.getElementById("error-message-number");

    if(serachInput == ""){
        errorInput.innerHTML = `<span style='color:#C22D39;'> Please enter search values </span>`;
        return false;
    } else if(numbersInput == 0){
        errorNumber.innerHTML = `<span style='color:#C22D39;'> You must pick a number!</span>`;
        return false;
    }else if(isNaN(numbersInput)){
        errorNumber.innerHTML = `<span style='color:#C22D39;'> Must be a number </span>`;
        return false;
    } else if( numbersInput > 15){
        errorNumber.innerHTML = `<span style='color:#C22D39;'> Max number is 15</span>`;
        return false;
    } else if(keyword1 == "" && keyword2 == "" && keyword3 == ""){
        displayKeywordInfo.innerHTML = `<span style='color:#C22D39;'>Du måste skriva in minst 1 nyckelord!</span>`;
        return false;
    }else{
        errorInput.innerHTML = `<span</span>`
        errorNumber.innerHTML = `<span</span>`
        document.getElementById("loader").style.display = "block";
        
        return true;
    }
}

// Check the scrape result
CheckOutput = () => {
    const pTag = document.getElementById("scrape-result");
    const keywordMessage = document.getElementById("keywordMessage");
    const errorMessage = document.getElementById("error-message");
    
    errorMessage.innerHTML = `<span></span>`
    keywordMessage.innerHTML = `<span>Nyckelord:</span>`

    if(pTag == null || pTag == "") errorMessage.innerHTML = `<span>Fann inget resultat baserat på det som matats in!</span>`;
}

document.addEventListener("DOMContentLoaded", () => {
    if(document.URL == "http://127.0.0.1:5000/search") CheckOutput();
})



