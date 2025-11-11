#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

typedef struct{
  vector<bool>g; //carros grandes
  vector<bool>p; //carros pequenos
} Espacios;

vector<bool> parkingB(8,0); //big parking spaces initialized on 0
vector<bool> parkingS(20,0); // small parking spaces initialized on 0
int carSize; //tamano del carro
int option; //opcion del usuario

vector<Espacios> parkingSpaces(4);

// FUNCTION PROTOTYPE
void available(void);
void entrance(void);
void exitpark(void);
bool checkAvailability(int type, int *piso, int *lugares);

int main()
{
  //iniciamos vacios los lugares
  for(int i = 0; i < parkingSpaces.size(); i++){
  parkingSpaces[i].g = vector<bool>(8, false);
  parkingSpaces[i].p = vector<bool>(20, false);
  }

  //bool para ciclo
  bool running = true;
  while(running == true){
    //bienvenida
    cout<<"== Welcome to park manager! ==\n";
    cout<<"select one of the following options: \n 1) Park your car \n 2) Exit parking spot \n 3) Check availability \n 4) Exit the parking system \n";
    cout<<"Your option: ";
    cin >> option;

    //opciones con su respectiva funcion
    switch (option){
      case 1:
      entrance();
      break;

      case 2:
      exitpark();
      break;

      case 3:
      available();
      break;

      //salida
      case 4:
      cout << "Thank you for using our system!";
      running = false;
      break;

      //opcion invalida
      default:
      cout << "Invalid Option" << endl << "Enter a valid option, please" << endl;
      break;
    }

    }
}

//revisar lugares disponibles
bool checkAvailability(int type, int *piso, int *lugares) //1 si es carro chico, 2 si es carro grande
{
  *piso = -1; //piso en el que se encontro un lugar
  *lugares = -1; //numero de lugares

  //primer busqueda para lugares segun el tipo de carro
  for(int i = 0; i < parkingSpaces.size(); i++){
    int numAvailable = 0;
      if(type == 1){
      numAvailable = count(parkingSpaces[i].p.begin(), parkingSpaces[i].p.end(), false);
      }
      else if(type == 2){
      numAvailable = count(parkingSpaces[i].g.begin(), parkingSpaces[i].g.end(), false);
    }
      if(numAvailable > 0){
        *piso = i;
        *lugares = numAvailable;
        return true;
      }
  }


  //si no hay luagares para el carro pequeno, se busca en los lugares disponibles de los grandes
  if(*piso == -1 && type == 1){
      for(int i = 0; i < parkingSpaces.size(); i++){
        int numAvailable = count(parkingSpaces[i].g.begin(), parkingSpaces[i].g.end(), false);
        if(numAvailable > 0){
          *piso = i;
          *lugares = numAvailable;
          return true;
      }
    }
  }
  return false;
}


//3) Check availability
//buscar los lugares disponibles, e imprimir cuantos hay en cada piso
    void available(){
    for(int i = 0; i < parkingSpaces.size(); i++){
      int bigAvailable = count(parkingSpaces[i].g.begin(), parkingSpaces[i].g.end(), false);
      int smallAvailable = count(parkingSpaces[i].p.begin(), parkingSpaces[i].p.end(), false);
      if(bigAvailable > 0 || smallAvailable > 0){
      cout<<"There are: "<< bigAvailable <<" big parking spots available &:"<<smallAvailable<<" small parking spots available in level: " << i << endl << endl;
    }
    else{
      cout<<"There are no parking spots available in level: " << i << endl << endl;
    }
  }
}

    //1) Park your car
    void entrance()
    {
      //elegir que carro se estacionara
      cout<<"Enter the option that best fits your car"<< endl; //en el gui estos serian botones :D
      cout<<"1) Small Car"<<endl;
      cout<<"2) Big Car"<<endl;
      cout<<"Your option: ";
      cin>>carSize;
      int piso, lugares;
      bool disponible = checkAvailability(carSize, &piso,&lugares);
      bool lugarasignado = false;

      //carros pequenos
      if(disponible == 1){
      switch (carSize){
        case 1:
        

        //Buscamos en el piso asigando un lugar de carros pequenos disponible
        cout << "There are: " << lugares << " ,in the floor: " << piso << endl;
        for(int i =0; i < parkingSpaces[piso].p.size(); i++){ 
        if (parkingSpaces[piso].p[i] == false){
          parkingSpaces[piso].p[i] = true;
          lugarasignado = true;
          cout << "You have parked your car in floor: " << piso << " in the space: " << i << endl;
          cout << "You parked in a small car space" << endl;
          break;
        }
        }

        //Si no hay lugares pequenos, se asigna un lugar de los carros grandes disponibles
        if(lugarasignado == false){
          for(int i =0; i < parkingSpaces[piso].g.size(); i++){ 
            if (parkingSpaces[piso].g[i] == false){
            parkingSpaces[piso].g[i] = true;
            lugarasignado = true;
            cout << "You have parked your car in floor: " << piso << " in the space: " << i << endl;
            cout << "You have parked in a big car space" << endl;
            break;
            }
          }
        }
        break;

        //se asignan lugares para los carros grandes
        case 2:
          cout << "There are: " << lugares << " ,in the floor: " << piso << endl;
          for(int i =0; i < parkingSpaces[piso].g.size(); i++){ 
          if (parkingSpaces[piso].g[i] == false){
            parkingSpaces[piso].g[i] = true;
            cout << "You have parked your car in floor: " << piso << " in the space: " << i << endl;
            cout << "You have parked in a big car space" << endl;
            break;
            }
          }
        break;

        default:
        cout << "Enter a valid size of Car, Please" << endl;
        break;
      }
    }
    else{
      cout << "There are no spaces for you to park your car" << endl;
    }
  }

//2) Exit Parking Spot
void exitpark(){
    cout<<"Enter the option that best fits your car for your exit"<< endl; //en el gui estos serian botones :D
    cout<<"1) Small Car"<<endl;
    cout<<"2) Big Car"<<endl;
    cout<<"Your option: ";
    cin>>carSize;

    //para sacar el carro correcto se le pide al usuario el piso y lugar
    int floor;
    cout << "Please enter the floor where you parked your car: ";
    cin >> floor;

    int place;
    cout << "Please enter the place where you parked your car: ";
    cin >> place;

    switch (carSize){

      //sacar un carro chico
      case 1:
      char typeplace;
      cout << "Did you parked in a big car space (y/n)? ";
      cin >> typeplace;
      if(typeplace != 'y'){
        if (parkingSpaces[floor].p[place] == true){
            parkingSpaces[floor].p[place] = false;
            cout << "You have removed your car from floor: " << floor << " in the space: " << place << endl;
          }
        else{
          cout << "The floor or the place you have entered, are not valid" << endl;
          cout << "Please verify your parking information" << endl;
        }
      }
      else{
        if (parkingSpaces[floor].g[place] == true){
            parkingSpaces[floor].g[place] = false;
            cout << "You have removed your car from floor: " << floor << " in the space: " << place << endl;
          }
        else{
          cout << "The floor or the place you have entered, are not valid" << endl;
          cout << "Please verify your parking information" << endl;
        }
      }
      break;

      //sacar un carro grande
      case 2:
        if (parkingSpaces[floor].g[place] == true){
              parkingSpaces[floor].g[place] = false;
              cout << "You have removed your car from floor: " << floor << " in the space: " << place << endl;
            }
          else{
            cout << "The floor or the place you have entered, are not valid" << endl;
            cout << "Please verify your parking information" << endl;
          }
      break;

      default:
      cout << "Enter a valid size of Car, Please" << endl;
      break;
    }
}
