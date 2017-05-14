#include<bits/stdc++.h>
using namespace std;
int main(){
	char pwd[21];
	int trytime=0,maxtime;
	cin>>pwd;
	cin>>maxtime;
	char usin[21];
	while(cin>>usin){
		if(usin[0]!='#'){
			trytime++;
			if(trytime>maxtime){
				cout<<"Account locked"<<endl;
				return 0;
			}
			else{
				if(strcmp(pwd,usin)==0){
					cout<<"Welcome in"<<endl;
					return 0;
				}else{
					cout<<"Wrong password: "<<usin<<endl;
				}
			}
		}
	}
} 
