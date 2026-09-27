const form = document.getElementById("researchForm");
const loader = document.getElementById("loader");

if(form){
    form.addEventListener("submit",()=>{
        loader.classList.remove("hidden");
    });
}

function copySummary(){

    const summary = document.querySelector("pre");

    navigator.clipboard.writeText(summary.innerText);

    alert("Summary copied successfully!");
}