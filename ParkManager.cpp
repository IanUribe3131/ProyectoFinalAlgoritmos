#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

typedef struct{
  vector<bool>g;
  vector<bool>p;
} Espacios;

vector<bool> parkingB(8,0); //big parking spaces initialized on 0
vector<bool> parkingS(20,0); // small parking spaces initialized on 0
int carSize;
int option;

vector<Espacios> parkingSpaces(4);

// FUNCTION PROTOTYPE
void available(void);
void entrance(void);

int main()
{
  for(int i = 0; i < parkingSpaces.size(); i++){
  parkingSpaces[i].g = vector<bool>(8, false);
  parkingSpaces[i].p = vector<bool>(20, false);
  }

  bool running = true;
  while(running == true){
    cout<<"== Welcome to park manager! ==\n";
    cout<<"select one of the following options: \n 1) Park your car \n 2) Exit parking spot \n 3) Check availability \n 4) Exit the parking system \n";
    cout<<"Your option: ";
    cin >> option;

    switch (option){
      case 1:
      break;

      case 2:
      break;

      case 3:
      available();
      break;

      case 4:
      cout << "Thank you for using our system!";
      running = false;
      break;

      default:
      cout << "Invalid Option" << endl << "Enter a valid option, please" << endl;
      break;
    }

    }
}

//3) Check availability
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
    void entrance(){
    cout<<"Enter 1) Small Car or 2) Big Car"<< endl; //en el gui estos serian botones :D
    cout<<"Your option: ";
    cin>>carSize;
    switch (carSize){
      case 1:
      break;

      case 2:
      break;

      default:
      cout << "Enter a valid size of Car, Please" << endl;
      break;
    }
  }