int ledPin =  12;    // LED connected to digital pin 12
int ledPin2 =  8;    // LED connected to digital pin 1
int ledPin3 =  2;    // LED connected to digital pin 0


void setup() {
  Serial.begin(9600);
  pinMode(ledPin,OUTPUT);    
  pinMode(ledPin2,OUTPUT);  
  pinMode(ledPin3,OUTPUT);  
}

void loop() {
  if (Serial.available() > 0) {
    char value = Serial.read();
    switch (value) {
      case  '1': 
        digitalWrite(ledPin, HIGH);
        break;
      case '2':
        digitalWrite(ledPin2, HIGH);
        break;
      case '3':
        digitalWrite(ledPin3, HIGH);
        break;
      case '4':
        digitalWrite(ledPin, HIGH);
        digitalWrite(ledPin2, HIGH);
        break;
      case '5':
        digitalWrite(ledPin, HIGH);
        digitalWrite(ledPin3, HIGH);
        break;
      case '6':
        digitalWrite(ledPin2, HIGH);
        digitalWrite(ledPin3, HIGH);
        break;
      case '7':
        digitalWrite(ledPin, HIGH);
        digitalWrite(ledPin2, HIGH);
        digitalWrite(ledPin3, HIGH);
        break;
      case '8':
        digitalWrite(ledPin, HIGH);
        break;
      case '9':
        digitalWrite(ledPin2, HIGH);
        break;
      case '10':
        digitalWrite(ledPin3, HIGH);
        break;
      case '11':
        digitalWrite(ledPin, HIGH);
        digitalWrite(ledPin2, HIGH);
        break;
      case '12':
        digitalWrite(ledPin2, HIGH);
        digitalWrite(ledPin3, HIGH);
        break;
      default:
        digitalWrite(ledPin, LOW);
        digitalWrite(ledPin2, LOW);
        digitalWrite(ledPin3, LOW);
    }
  }
}
