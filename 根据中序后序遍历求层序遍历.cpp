#include<iostream>
#include<queue>
using namespace std;
struct node {
	int data;
	node* lchild;
	node* rchild;
};
int post[50];
int in[50];
int pre[50];
int n;
node* create(int posL, int posR, int inL, int inR) {
	if (posL > posR)
		return NULL;
	node* root = new node;
	root->data = post[posR];/*根据前序遍历或者后序遍历的特点找到树根结点的值，再去中序遍历序列中寻找树根，从而分开左右两棵子树*/
	int k = 0;
	for (k = inL; k <= inR; k++ ) {/*左右都要访问到，所以<=inR*/
		if (post[posR] == in[k]) {
			break;
		}
	}
	int numLeft = k - inL;
	root->lchild = create(posL, posL + numLeft - 1, inL, k - 1);/*关键确定左右两颗子树的起点和重点*/
	root->rchild = create(posL + numLeft, posR-1, k + 1, inR);/*后序遍历的右子树最后一个值是根结点，所以注意要去掉*/
	return root;
}
void BFS(node* root) {
	int num = 0;
	queue<node*> q;
	q.push(root);
	while (!q.empty()) {
		node* now = q.front();
		q.pop();/*取完队前的front值，还要把队前pop出来才行*/
		cout << now->data;
		if (++num< n) cout << " ";/*此处控制格式，最后一个不空格*/
		if(now->lchild!=NULL) q.push(now->lchild);
		if(now->rchild!=NULL) q.push(now->rchild);/*注意是当前节点now的子节点，不要弄混了*/
	}
}
int main() {
	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> post[i];
	}
	for (int i = 0; i < n; i++) {
		cin >> in[i];
	}
	node* tree = create(0, n - 1, 0, n - 1);
	BFS(tree);
}
