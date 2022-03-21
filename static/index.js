// Check input values and loading 
const searchButton = document.getElementById("search-button");

searchButton.addEventListener('click', (event) => {
    let serachInput = document.forms["search_form"]["search-input"].value
    let numbersInput = Number(document.forms["search_form"]["amount-of-pages"].value)
    let keyword1 = document.forms["search_form"]["input-keyword1"].value;
    let keyword2 = document.forms["search_form"]["input-keyword2"].value;
    let keyword3 = document.forms["search_form"]["input-keyword3"].value;
    let displayKeywordInfo = document.getElementById("keyword-info");
    let errorInput = document.getElementById("error-message-input");
    let errorNumber = document.getElementById("error-message-number");

    if(serachInput == ""){
        event.preventDefault()
        errorInput.innerHTML = `<span style='color:#C22D39;'> Please enter search values </span>`;
    } else if(numbersInput == 0){
        event.preventDefault()
        errorNumber.innerHTML = `<span style='color:#C22D39;'> You must pick a number!</span>`;
    }else if(isNaN(numbersInput)){
        event.preventDefault()
        errorNumber.innerHTML = `<span style='color:#C22D39;'> Must be a number </span>`;
    } else if( numbersInput > 15){
        event.preventDefault()
        errorNumber.innerHTML = `<span style='color:#C22D39;'> Max number is 15</span>`;
    } else if(keyword1 == "" && keyword2 == "" && keyword3 == ""){
        event.preventDefault()
        displayKeywordInfo.innerHTML = `<span style='color:#C22D39;'>Du måste skriva in minst 1 nyckelord!</span>`;
    } else{
        errorInput.innerHTML = `<span</span>`
        errorNumber.innerHTML = `<span</span>`
        document.getElementById("loader").style.display = "block";
    }
    
})

// Check the scrape result
CheckOutput = () => {
    const pTag = document.getElementById("scrape-result");
    const keywordMessage = document.getElementById("keyword-message");
    const errorMessage = document.getElementById("error-message");
    const searchMessage = document.getElementById("searchword-message");
    
    errorMessage.innerHTML = `<span></span>`
    searchMessage.innerHTML = `<strong><span>Sökord:</span></strong>` 
    keywordMessage.innerHTML = `<strong><span>Nyckelord:</span></strong>`

    if(pTag == null || pTag == "") errorMessage.innerHTML = `<span>Fann inget resultat baserat på det som matats in!</span>`;
}

document.addEventListener("DOMContentLoaded", () => {
    if(document.URL == "http://127.0.0.1:5000/search") CheckOutput();
})



