// chiamiamo data_table l'ogetto con le password

//data_table = sessionStorage.data_table

data_table = {
    pass:"tobia",
    user:"aibot"};
let main = document.querySelector("main");
if (Object.keys(data_table).length === 0){
    main.innerHTML += '<div id="no-groups">no password has been added yet, use the add command to add some!</div>';
}
let i=0;
main.innerHTML+= '<ul></ul>';
let ul = document.querySelector("main ul");
for (group in data_table){
    ul.innerHTML += '<li><button>' + group + '</button></li>';
}
