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
}