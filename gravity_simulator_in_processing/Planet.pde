class Planet {

  float radius;
  float angle;
  float distance;
  Planet[] planets;
  float orbitSpeed;

  Planet(float r, float d, float o) {
    radius = r;
    distance = d;
    angle = random(TWO_PI);
    orbitSpeed = o;
  }

  void orbit() {
    angle += orbitSpeed; 
  }

  void show() {
    fill(255, 100);
    rotate(angle);
    translate(distance, 0);
    ellipse(0, 0, radius*2, radius*2); 
  }
}
