// Check input values and loading 
const searchButton = document.getElementById("search-button");
const highlightWordsButton = document.getElementById("btn_highlight_keywords");
const removeMarkButton = document.getElementById("btn-remove-mark");
const saveExcelButton = document.getElementById("btn_save_excel");

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

document.addEventListener('DOMContentLoaded', () => {
    if(document.URL == "http://127.0.0.1:5000/"){
        highlightWordsButton.style.backgroundColor = "#808080";
        highlightWordsButton.disabled = true
        removeMarkButton.style.backgroundColor = "#808080";
        removeMarkButton.disabled = true
        saveExcelButton.style.backgroundColor = "#808080";
        saveExcelButton.disabled = true
    }
})

document.addEventListener("click", () => {
    if(document.URL == "http://127.0.0.1:5000/search") {
        CheckOutput();
        highlightWordsButton.style.backgroundColor = "rgb(38, 93, 61)";
        highlightWordsButton.disabled = false
        removeMarkButton.style.backgroundColor = "rgb(38, 93, 61)";
        removeMarkButton.disabled = false
        saveExcelButton.style.backgroundColor = "rgb(38, 93, 61)";
        saveExcelButton.disabled = false
    }
})


highlightWordsButton.addEventListener('click', (event) => {
    event.preventDefault();
    HighlightWords();
})

removeMarkButton.addEventListener('click', (event) => {
    event.preventDefault();
    RemoveMark();
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


RemoveMark = () => {
    let scrape_result = document.getElementsByClassName("all-scrape")
    for(let i=0; i < scrape_result.length; i++){
        let data = scrape_result[i].textContent;
        let sentences = scrape_result[i];

        sentences.innerHTML = data.replace(
            sentences, data => `<p>${data}</p><br>`
        )

    }
}

HighlightWords = () => {

    let scrape_result = document.getElementsByClassName("all-scrape")
    let user_keywords = document.getElementsByClassName("each-keyword")

    for(let i=0; i < scrape_result.length; i++){
        const words = [
            user_keywords[0].textContent.trim(),
            user_keywords[1].textContent.trim(),
            user_keywords[2].textContent.trim()
        ]

        var regexMetachars = /[(){[*+?.\\^$|]/g;
        for(let i=0; i < words.length; i++){
            words[i] = words[i].replace(regexMetachars, "\\$&");
        }
        
        let sentences = scrape_result[i]
        var regex = new RegExp("\\b(?:" + words.join("|") + ")\\b", "gi")
        
        sentences.innerHTML = sentences.textContent.replace(
            regex, match => `<mark>${match}</mark>`
        )
    
    }
}