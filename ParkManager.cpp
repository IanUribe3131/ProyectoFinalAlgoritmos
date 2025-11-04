#include <iostream>
#include <vector>
#include <string>

using namespace std;

int bigAvailable = 8;
int smallAvailable = 20;
vector<int> parkingB(8,0); //big parking spaces initialized on 0
vector<int> parkingS(20,0); // small parking spaces initialized on 0
string carSize;

int main(){
  cout<<"== Welcome to park manager! ==\n";
  cout<<"select one of the following options: \n 1) Park car \n 2) Exit parking spot \n 3) Check availability \n";

  ;

  }

void available(){
  if(bigAvailable > 0 || smallAvailable > 0){
    cout<<"There are "<< bigAvailable <<" big parking spots available & "<<smallAvailable<<"small parking spots available";
  }
  else{
    cout<<"There are no parking spots available in this moment";
  }
}

void entrance(){
  cout<<"Is your car big or small? \n"; //en el gui estos serian botones :D
  cin>>carSize;
  if(carSize)
}