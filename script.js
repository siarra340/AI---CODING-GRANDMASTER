class Superhero {
    constructor(name, power, mission) {
        this.name = name;
        this.power = power;
        this.mission = mission;
    }


describeHero(){
    return "<div class= 'hero-card'>" +
    "<p class= 'hero-name'>"+ 
    this.name + "</p>" +
    "<p class= 'hero-power'>"+ "Power: "+
    this.power + "</p>" +
    "<p class= 'hero-mission'>" + "Misson: " + this.mission + "</p>" + 
   
    "</div>"
    }
}

function showHeroes(){
    let hero1 = new Superhero(
        "Captain Code",
        "Debugging errors",
        "Fix broken programs and save the coding world."
    );

    let hero2= new Superhero(
        "Pixel Flash",
        "Super speed desgin",
        "Build colourful websites in seconds."
    );

    let hero3= new Superhero(
        "Logic Girl",
        "Smart problem-solving",
        "Use logic to solve tricky challanges"
    );

    let hero4= new Superhero(
        "Data Knight",
        "Data protection",
        "Keep inmportant information safe."
    );

    document.getElementById("heroCards").innerHTML=
    hero1.describeHero()+
    hero2.describeHero()+
    hero3.describeHero()+
    hero4.describeHero();
}