#include<bits/stdc++.h>
using namespace std;
int photo[510][510];
void printout(int m){
	if(m>=100){
		cout<<m;
	}else if(m>=10&&m<100){
		cout<<"0"<<m;
	}else{
		cout<<"00"<<m;
	}
}
int main(){
	int M,N;
	int A,B;
	int k;
	cin>>M>>N>>A>>B>>k;
	for(int i=0;i<M;i++){
	   for(int j=0;j<N;j++){
	   	   int tem;
	   	   cin>>tem;
	   	   if(tem>=A&&tem<=B){
	   	   	    printout(k);
			}
			else{
				printout(tem);
			}
			if(j<M-1) cout<<" ";
	   }
	   cout<<endl;
	}
}
