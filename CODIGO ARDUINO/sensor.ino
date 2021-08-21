//Mandamos a llamar la librería que interpreta los comandos del sensor
#include "FPS_GT511C3.h"
 //Utilizamos la librería que manipula el puerto serial
#include "SoftwareSerial.h"

//Configuramos los pines 4 y 5 como Rx, Tx
FPS_GT511C3 fps(4, 5); 
String inputString = "";
void setup() {
  Serial.begin(9600); 
  // put your setup code here, to run once:
  //Definimos un retardo de 100 ms
  delay(100);
//Abrimos la conexión con el sensor biométrico
  fps.Open();
//Actibamos el led interno del sensor biométrico
  fps.SetLED(true);
//Con este comando borramos la base de datos del sensor biométrico
//fps.DeleteAll();

}

void loop() {
  // put your main code here, to run repeatedly:
  while (Serial.available() > 0){
    char recibido = Serial.read();
    inputString += recibido;
    if( recibido == '\n' ){
      char code = inputString[0];
//Elije la funcion que se va a ejecutar
      switch(code){
        case 'H': OneFunction();break;
        case 'L': TwoFunction();break;
        case 'D': ThreeFunction(inputString);break;
        case 'E': FourFunction(); break;
      }
      inputString = "";
    }
   }
  }
void FourFunction(){
//Esta funcion borra los registros existentes en el sensor
  int result = fps.DeleteAll();
  Serial.print("success:");
  Serial.println(result);
}
void OneFunction(){
//Esta funcion registra una huella en la base de datos
  int enrollid = 0;
    bool usedid = true;
    while (usedid == true)
    {
      usedid = fps.CheckEnrolled(enrollid);
      if (usedid==true) enrollid++;
    }
    fps.EnrollStart(enrollid);
    Serial.print("Presione su dedo para registrar #");
    Serial.println(enrollid);
    while(fps.IsPressFinger() == false) delay(100);
    bool bret = fps.CaptureFinger(true);
    int iret = 0;
    if (bret != false)
    {
      Serial.println("Remover dedo");
      fps.Enroll1();
      while(fps.IsPressFinger() == true) delay(100);
      Serial.println("Presione el mismo dedo");
      while(fps.IsPressFinger() == false) delay(100);
      bret = fps.CaptureFinger(true);
      if (bret != false)
      {
          Serial.println("Remover dedo");
          fps.Enroll2();
          while(fps.IsPressFinger() == true) delay(100);
          Serial.println("Presionar el mismo dedo");
          while(fps.IsPressFinger() == false) delay(100);
          bret = fps.CaptureFinger(true);
          if (bret != false)
          {
            Serial.println("Remover dedo");
            iret = fps.Enroll3();
            if (iret == 0)
            {
              Serial.print("registrado:");
              Serial.println(enrollid);//registro que se envia a la base datos
            }
            else
            {
              Serial.print("error:");
              Serial.println(iret);
            }
           }
          else Serial.println("error:Failed to capture third finger");
         }
         else Serial.println("error:Failed to capture second finger");
        }
        else Serial.println("error:Failed to capture first finger");
        }
void TwoFunction(){
//Esta funcion verifica las huellas registradas en el sistema
    while(true){
      if (fps.IsPressFinger()){
       fps.CaptureFinger(false);
       int id = fps.Identify1_N();
       if (id < 200){
          Serial.print("success:");
          Serial.println(id);
          break;
        }else{
            Serial.println("error:Finger not found");
            break;
         }
         }else{
            Serial.println("Please press finger");
          }
          delay(500);
        }
      }
void ThreeFunction(String response){
//Esta funcion borra Ids especificos registrados en el sistema
    String ids = response.substring(1);
    int returns = fps.DeleteID(ids.toInt());
    Serial.print("response:");
    Serial.println(returns);
    }
