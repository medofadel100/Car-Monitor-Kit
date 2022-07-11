var firewbl = document.getElementById("wbl ");
var firewbr = document.getElementById("wbr ");
var firewfl = document.getElementById("wfl ");
var firewfr = document.getElementById("wfr ");
var firespeed;

var firebasewblRef = firebase.database().ref().child("wbl");
var firebasewbrRef = firebase.database().ref().child("wbr");
var firebasewflRef = firebase.database().ref().child("wfl");
var firebasewfrRef = firebase.database().ref().child("wfr");
var firebasespeedRef = firebase.database().ref().child("speed");

firebasewblRef.on('value', function(datasnapshot) {
    firewbl.innerText = datasnapshot.val();

});

firebasewbrRef.on('value', function(datasnapshot) {
    firewbr.innerText = datasnapshot.val();

});

firebasewflRef.on('value', function(datasnapshot) {
    firewfl.innerText = datasnapshot.val();

});

firebasewfrRef.on('value', function(datasnapshot) {
    firewfr.innerText = datasnapshot.val();

});

firebasespeedRef.on('value', function(datasnapshot) {
    $('canvas').attr("data-value", datasnapshot.val());
})