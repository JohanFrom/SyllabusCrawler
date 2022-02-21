CheckInput = () => {
    const form = document.forms["search_form"]["search-input"].value
    if(form == ""){
        let error = document.getElementById("error-message");
        error.innerHTML = `<span style='color:#C22D39;'> Please enter search values </span>`;
        return false;
    }
}