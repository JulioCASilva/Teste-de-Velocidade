#include <iostream>
#include <chrono>
using namespace std;
using namespace std::chrono;
int main() {
cout << "Olá mundo\n"; //imprimir Olá mundo

//inicio da contagem de numero de 1 ate 1000
cout << "Inicio da contagem:\n";

for(int c = 1; c <= 1000; c ++){
       cout << c << endl;
}
//final da contagem de numero de 1 ate 1000

//inincio da contagem de tempo
auto inicio = high_resolution_clock::now();

int x = 0;

while (x < 100000000) {
  x = x + 1;
}

auto fim = high_resolution_clock::now();
double total = duration_cast<microseconds>(fim-inicio).count();
cout << "Tempo total: " << std::fixed << (total/1000000); //imprimir o tempo
//final da contagem de tempo

return 0;
}