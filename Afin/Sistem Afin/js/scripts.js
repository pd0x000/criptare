let criptedArray = new Array();
let charImages = new Array();
let alphabet2 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"];

function posibleValuesFor_a(){
    let n = parseInt(document.getElementById("n").value);
   let arrayA = new Array();
   for (let i=1 ; i<=n; i++){
      if( n % i == 0 || i % 2 == 0){
         continue;
      }else arrayA.push(i);
      }
document.getElementById("posibleValues").innerHTML = "Lista de valori posibile lui a : " + arrayA;
}

var textCriptat = document.getElementById("textcr1").value.toUpperCase();


function cript(){
   let n = parseInt(document.getElementById("n").value);
   let a = parseInt(document.getElementById("a").value);
   let b = parseInt(document.getElementById("b").value);
   criptedArray = [];
   charImages = [];
   document.getElementById("textcl").value = document.getElementById("textcl").value.toUpperCase();
   var textClar = document.getElementById("textcl").value.toUpperCase();
   document.getElementById("textcr").value = "";
   let ek = 0;
   for (let i = 0 ; i <=textClar.length - 1 ; i++){
      /*alert("Character index = " + alphabet2.indexOf(textClar.charAt(i)));*/
      charImages.push(alphabet2.indexOf(textClar.charAt(i)));
   }
   for (let i = 0 ; i <= charImages.length - 1 ; i++){
      ek = (a * charImages[i] + b) % n ;
      /*alert("ek ="+ ek +" char = " + alphabet2[ek])*/
      criptedArray.push(alphabet2[ek]);
   }
   document.getElementById("textcr").value = criptedArray.join('');
}

let clearMessage = new Array();
let a_invers =0;

function decript(){
   inversa_a();
   let n = parseInt(document.getElementById("n").value);
   let a = parseInt(document.getElementById("a").value);
   let b = parseInt(document.getElementById("b").value);
   charImages = [];
   clearMessage =[];
   document.getElementById("textcr1").value = document.getElementById("textcr1").value.toUpperCase();
   var textCriptat = document.getElementById("textcr1").value.toUpperCase();
   document.getElementById("textcl1").value = "";
   let dk =0;
   for (let i = 0 ; i <= textCriptat.length -1 ; i++){
      charImages.push(alphabet2.indexOf(textCriptat.charAt(i)));
   }
   for (let i = 0 ; i <= charImages.length - 1 ; i++){
      dk = (a_invers * charImages[i] + a_invers * (n - b)) % n ;
      /*alert("ek ="+ ek +" char = " + alphabet2[ek])*/
      clearMessage.push(alphabet2[dk]);
   }
   document.getElementById("textcl1").value = clearMessage.join('');

}


function inversa_a(){
   let n = parseInt(document.getElementById("n").value);
   let a = parseInt(document.getElementById("a").value);
   let b = parseInt(document.getElementById("b").value);
   let n0 = n;
   let a0 = a;
   let t0 = 0;
   let t = 1;
   let q = Math.trunc(n0/a);
   let r = n0 -q * a;
   while (r > 0){
      let temp = t0 -q * t;
      if (temp >= 0){
         temp = temp % n;
      }else{
         temp = n - ((0-temp) % n);
      }
         n0 = a0;
         a0 = r;
         t0 = t;
         t = temp;
         q = Math.trunc(n0/a0);
         r = n0 - q * a0;
   }
   if (a0 != 1){
      alert(a + " nu are inversa mod " + n);
      //document.getElementById("textcl1").value = a + " nu are inversa mod " + n;
   }else{
      a_invers = t ;
   }
}

function hideSettings(){
   document.getElementById("settings").style.visibility = "hidden"; 
}

function showSettings() {
   document.getElementById("settings").style.visibility = "visible"; 
}

function hideEncrypt(){
   document.getElementById("encrypt").style.visibility = "hidden"; 
}

function showEncrypt() {
   document.getElementById("encrypt").style.visibility = "visible"; 
}

function hideDecrypt(){
   document.getElementById("decrypt").style.visibility = "hidden"; 
}

function showDecrypt() {
   document.getElementById("decrypt").style.visibility = "visible"; 
}

function hide() {
   hideDecrypt();
   hideEncrypt();
   hideSettings();
}

function clearDecrypt(){
   clearMessage = [];
   charImages = []
   document.getElementById("textcl1").value = "";
   document.getElementById("textcr1").value = "";
}

function clearEncrypt(){
   clearMessage = [];
   criptedArray = []
   document.getElementById("textcl").value = "";
   document.getElementById("textcr").value = "";
}

function clearSettings(){
   arrayA = [];
   document.getElementById("a").value = "";
   document.getElementById("b").value = "";
   document.getElementById("n").value = "";
   document.getElementById("posibleValues").innerHTML = "";
}