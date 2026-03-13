const existingLoan = document.getElementById("existingLoan");
const loanDetails = document.getElementById("loanDetails");

existingLoan.addEventListener("change", function(){

if(existingLoan.value === "yes"){
loanDetails.style.display = "block";
}
else{
loanDetails.style.display = "none";
}

});


const creditCard = document.getElementById("creditCard");
const creditScoreField = document.getElementById("creditScoreField");

creditCard.addEventListener("change", function(){

if(creditCard.value === "yes"){
creditScoreField.style.display = "block";
}
else{
creditScoreField.style.display = "none";
}

});