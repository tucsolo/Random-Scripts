/*
  Ruota della Fortuna  ~~~  Fortune Wheel
  ---------------------------------------
  
  Emanuele Savo (tucs) for Roma2LUG
  emanuele.savo@gmail.com
  
  Free Software --- GPLv3
  
 */
 
//  Pins
int a0 = 4;
int a1 = 5;
int b0 = 6;
int b1 = 7;

// the setup routine runs once when you press reset:
void setup() {                
  // initialize the digital pin as an output.
  pinMode(a0, OUTPUT);
  pinMode(a1, OUTPUT)
  pinMode(b0, OUTPUT);
  pinMode(b1, OUTPUT);

}

// the loop routine runs over and over again forever:
void loop() {
}
void p0()
{
  digitalWrite(a0, LOW);
  digitalWrite(a1, LOW);
  digitalWrite(b0, LOW);
  digitalWrite(b1, LOW);
}

void p1()
{
  digitalWrite(a0, LOW);
  digitalWrite(a1, LOW);
  digitalWrite(b0, LOW);
  digitalWrite(b1, HIGH);
}
void p2()
{
  digitalWrite(a0, LOW);
  digitalWrite(a1, LOW);
  digitalWrite(b0, HIGH);
  digitalWrite(b1, LOW);
}
void p3()
{
  digitalWrite(a0, LOW);
  digitalWrite(a1, LOW);
  digitalWrite(b0, HIGH);
  digitalWrite(b1, HIGH);
}

void p4()
{
  digitalWrite(a0, LOW);
  digitalWrite(a1, HIGH);
  digitalWrite(b0, LOW);
  digitalWrite(b1, LOW);
}

void p5()
{
  digitalWrite(a0, LOW);
  digitalWrite(a1, HIGH);
  digitalWrite(b0, LOW);
  digitalWrite(b1, HIGH);
}
void p6()
{
  digitalWrite(a0, LOW);
  digitalWrite(a1, HIGH);
  digitalWrite(b0, HIGH);
  digitalWrite(b1, LOW);
}
void p7()
{
  digitalWrite(a0, LOW);
  digitalWrite(a1, HIGH);
  digitalWrite(b0, HIGH);
  digitalWrite(b1, HIGH);
}
void p8()
{
  digitalWrite(a0, HIGH);
  digitalWrite(a1, LOW);
  digitalWrite(b0, LOW);
  digitalWrite(b1, LOW);
}

void p9()
{
  digitalWrite(a0, HIGH);
  digitalWrite(a1, LOW);
  digitalWrite(b0, LOW);
  digitalWrite(b1, HIGH);
}
void pa()
{
  digitalWrite(a0, HIGH);
  digitalWrite(a1, LOW);
  digitalWrite(b0, HIGH);
  digitalWrite(b1, LOW);
}
void pb()
{
  digitalWrite(a0, HIGH);
  digitalWrite(a1, LOW);
  digitalWrite(b0, HIGH);
  digitalWrite(b1, HIGH);
}

void pc()
{
  digitalWrite(a0, HIGH);
  digitalWrite(a1, HIGH);
  digitalWrite(b0, LOW);
  digitalWrite(b1, LOW);
}

void pd()
{
  digitalWrite(a0, HIGH);
  digitalWrite(a1, HIGH);
  digitalWrite(b0, LOW);
  digitalWrite(b1, HIGH);
}
void pe()
{
  digitalWrite(a0, HIGH);
  digitalWrite(a1, HIGH);
  digitalWrite(b0, HIGH);
  digitalWrite(b1, LOW);
}
void pf()
{
  digitalWrite(a0, HIGH);
  digitalWrite(a1, HIGH);
  digitalWrite(b0, HIGH);
  digitalWrite(b1, HIGH);
}

void loopa(int timea)
{
  p0();
  delay(timea);
  p1();
  delay(timea);
  p2();
  delay(timea);
  p3();
  delay(timea);
  p4();
  delay(timea);
  p5();
  delay(timea);
  p6();
  delay(timea);
  p7();
  delay(timea);
  p8();
  delay(timea);
  p9();
  delay(timea);
  pa();
  delay(timea);
  pb();
  delay(timea);
  pc();
  delay(timea);
  pd();
  delay(timea);
  pe();
  delay(timea);
  pf();
  delay(timea);
}

void switchl(int val)
{
  if (val == 0){ p0();}
  if (val == 1){ p1();}
  if (val == 2){ p2();}
  if (val == 3){ p3();}
  if (val == 4){ p4();}
  if (val == 5){ p5();}
  if (val == 6){ p6();}
  if (val == 7){ p7();}
  if (val == 8){ p8();}
  if (val == 9){ p9();}
  if (val == 10){ pa();}
  if (val == 11){ pb();}
  if (val == 12){ pc();}
  if (val == 13){ pd();}
  if (val == 14){ pe();}
  if (val == 15){ pf();}
}
