#include<iostream>
#include<algorithm>
#include<cstdio>
using namespace std;
const int maxnum = 100;
int f[maxnum][maxnum];
int dp[maxnum][maxnum];
int main(){
	int n;
	cin >> n;
	for (int i = 1;i <=n; i++) {
		for (int j = 1; j <= i; j++) {
			cin >> f[i][j];
		}
	}
	for (int i = 1; i <= n; i++) {
		dp[n][i] = f[n][i];
	}
	for (int i = n - 1; i >= 1; i--) {
		for (int j = 1; j <= i; j++) {
			dp[i][j] = (dp[i + 1][j] > dp[i + 1][j + 1] ? dp[i + 1][j] : dp[i + 1][j + 1]) + f[i][j];//状态转移方程-core
		}
	}
	cout << dp[1][1];
}