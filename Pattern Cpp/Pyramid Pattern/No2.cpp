#include<iostream>
using namespace std;
int main(){
          int n = 3;
          int i,j;
          for(i = 0; i < n; i++){
                    for(j = 0; j<n-i-1; j++){
                              cout<<" ";
                    }
                    //nums1;i+1
                    for(j = 1; j<=i+1; j++){
                              cout<< j;
                    }
                    //num2;
                    for (j = i; j>0; j--){
                              cout<< j;
                    }
                    cout<< endl;
          }
          return 0;
}