
void setup() {
    //Setting up serial parameters
    Serial.begin(115200);
}

void loop() {
    int*  serialIntData = ReadSerialConnection();
    delete[] serialIntData;
}

int* ReadSerialConnection(void){
    int arrayCounter = 0;
    int iterationCounter = 0;
    int* serialIntData = new int[maxMessageSize];
    memset(serialIntData, 0, maxMessageSize);
    //Serial.println(String(serialIntData[0]) + ' ' + String(serialIntData[2]));
    String serialData[maxMessageSize];
    while (Serial.available() > 0){
      char readByte = Serial.read();
      if (readByte != '&' and iterationCounter <= maxMessageSize){
        if (readByte == ','){
            serialIntData[arrayCounter] = serialData[arrayCounter].toInt();
            Serial.println(serialData[arrayCounter].toInt());
            arrayCounter++;
        }
        else{
            serialData[arrayCounter] += readByte;
        }
        iterationCounter++;
      }
      // breaking the loop if end of array has been reached or max length is exceeded
      else{
            break;
      }
   }
   Serial.println(String(serialIntData[0]) + ' ' + String(serialIntData[2]));
   return serialIntData;
}