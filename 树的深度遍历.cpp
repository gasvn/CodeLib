#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
int n, m, s;//节点数 边数 给定的和
int path[110];
struct node {
	int weight;
	vector<int> child;
}Node[110]; //采用树的静态写法
bool cmp(int a,int b) {
	if (Node[a].weight > Node[b].weight)
		return true;
	return false;
}
/*树的深度遍历算法，*/
void DFS(int index, int numNode, int sum) {
	if (sum > s) return;
	if (sum == s) {//在满足条件后把path中的编号对应节点的值输出
		if (Node[index].child.size() != 0) return;
		for (int i = 0; i < numNode; i++) {
			cout << Node[path[i]].weight;
			if (i < numNode - 1)  cout << " ";
			else cout << endl;
		}
	}
	for (int i = 0; i < Node[index].child.size(); i++) {// 每次从孩子中继续向下一级遍历，把节点的标号存到path中。到达本层，第二次循环会把第一次循环的path后面的内容覆盖
		int child = Node[index].child[i];
		path[numNode] = child;
		DFS(child, numNode + 1, sum + Node[child].weight);
	}
}
int main() {
	cin >> n >> m >> s;
	for (int i = 0; i < n; i++) {
		cin >> Node[i].weight;
	}
	int id, k, child;
	for (int i = 0; i < m; i++) {
		cin >> id >> k;
		for (int j = 0; j < k; j++) {
			cin >> child;
			Node[id].child.push_back(child);
		}
		sort(Node[id].child.begin(), Node[id].child.end(), cmp);
	}
	path[0] = 0;
	DFS(0, 1, Node[0].weight);
}