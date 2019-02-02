function codejoy(){
    console.log("codejoy custom function fired");
    let spot = document.getElementById("test");
    let other = document.getElementById("grow");
    if(other){
        other.id = 'test';
    }else{
        spot.id="grow"
    }
}