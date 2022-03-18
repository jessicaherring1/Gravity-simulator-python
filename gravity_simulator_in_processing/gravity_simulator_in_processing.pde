Planet p1 = new Planet(50, 0, 0);
Planet p2 = new Planet(25, 100, 0.02);
Planet p3 = new Planet(10, 175, .02);
Planet p4 = new Planet(5, 50, .02);


/*Planet p1 = new Planet(25, 100, 0.02);
Planet p2 = new Planet(10, 175, .02);
Planet p3 = new Planet(50, 0, 0);
Planet p4 = new Planet(5, 50, .02); */
Planet[] planets = { p1, p2, p3, p4};


void setup() {
  size(600, 600);
}


void draw() {
  background(0);
  translate(width/2, height/2);
  if (planets!=null) {
    for (int i=0; i<planets.length; i++) {
      planets[i].show();
      planets[i].orbit();
      //updateGravity();
    }
  }
}


void updateGravity() {
  /*if (planets != null) {
   for (Planet p1 : planets) {
   for (Planet p2 : planets) {
   if (p1 != p2) {
   if (p1.radius < p2.radius) {
   float d = abs(p1.distance - p2.distance);
   p1 = new Planet(p1.radius, d, p1.orbitSpeed);
   } else {
   float d = abs(p1.distance - p2.distance);
   p2 = new Planet(p2.radius, d, p2.orbitSpeed);
   }
   }
   }
   }
   }*/

  if (planets != null) {
    for (int i=0; i<planets.length -1; i++) {
      if (planets[i+1] != null) {
        for (int j= i+1; j < planets.length; j++) {
          if (planets[i].radius < planets[j].radius) {
            float d = abs(planets[i].distance - planets[j].distance);
            planets[i] = new Planet(planets[i].radius, d, planets[i].orbitSpeed);
          } else {
            float d = abs(planets[i].distance - planets[j].distance);
            planets[j] = new Planet(planets[j].radius, d, planets[j].orbitSpeed);
          }
        }
      }
    }
  }
}
